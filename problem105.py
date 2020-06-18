# Problem #105

# Given a function f, and N return a debounced f of N milliseconds.
#
# That is, as long as the debounced f continues to be invoked, f itself will not be called for N milliseconds.

from threading import Timer
import time
from datetime import datetime


def debounce(wait):
    """ https://gist.github.com/walkermatt/2871026
        Decorator that will postpone a functions
        execution until after wait seconds
        have elapsed since the last time it was invoked. """

    wait = wait / 1000

    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = Timer(wait, call_it)
            debounced.t.start()
        return debounced
    return decorator


@debounce(500)
def hello_world():
    print(f"Hello World!  {int(round(time.time() * 1000))}")


hello_world()
time.sleep(.6)
hello_world()
time.sleep(.1)
hello_world()
time.sleep(.3)
hello_world()
time.sleep(.2)
hello_world()

# never heard about debounce, looked online and found this implementation, have just to chance it to milliseconds.
# I understand why this exists and its functionality, but its implementation still a little bit confusing

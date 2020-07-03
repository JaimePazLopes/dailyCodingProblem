# Problem #120
#
# Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
# And in every even call of getInstance(), return the first instance and in every odd call of getInstance(),
# return the second instance.


class Singleton:

    _instances = None
    _next = True

    @classmethod
    def instance(cls):
        if cls._instances is None:
            cls._instances = list()
            cls._instances.append(cls())
            cls._instances.append(cls())

        cls._next = not cls._next
        return cls._instances[cls._next]


first = Singleton.instance()
second = Singleton.instance()
third = Singleton.instance()
fourth = Singleton.instance()

assert first is not second
assert first is third
assert second is fourth
assert second is not third

# this was my first try with singleton in python, i dont know if there is a more standard way to do it. everyone online
# looks like is doing it in a different way

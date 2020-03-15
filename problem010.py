# Problem #10 [Medium]
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time

def scheduler(function, timeToWait):
    time.sleep(timeToWait/1000)
    function()

def helloWorld():
    print("Hello World")

scheduler(helloWorld, 1000)

# took less than 5 minutes, weird problem to ask, specially saying that this is medium difficulty

# this time the function can have parameters with kargs and return the value of the function
def schedulerKargs(timeToWait, function, **kargs):
    time.sleep(timeToWait/1000)
    return function(**kargs)

# this time the function can have parameters with args and return the value of the function
def schedulerArgs(timeToWait, function, *args):
    time.sleep(timeToWait / 1000)
    return function(*args)

# creating a new function that has parameters
def helloWorldComplex(message, number):
    for _ in range(number):
        print(f"Hello World! {message}")

schedulerArgs(200, helloWorld)
schedulerKargs(200, helloWorld)
schedulerArgs(500,helloWorldComplex, "Message End", 2)
schedulerKargs(1000,helloWorldComplex, number = 5, message = "Thanks")
schedulerArgs(500,print, "My favorite number is ", 33, "but I also like ", 7, "and", 999)
print(f"The maximum is {schedulerArgs(2000, max, 10, 2)}")

# since it was fast i decided to play a little with this idea, all work took less than 30 minutes

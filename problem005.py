# Problem #5 [Medium]
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
# Given this implementation of cons:

# ok, took much more time than I should need to understand this, not fully dominating python got in the way
# cons is a function that has a nested function and its return value is its nested function
# this nested function take a function as parameters and execute it with a, b as arguments
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# this pair is not actually a pair, its not something like an array or list, it is a function that needs to be called
# more than that this function need to be called passing another function, and this function must have 2 parameters
# to solve this, its necessary to implement 2 functions, one that return the first value and another for the second
# on this case I decided to go with lambda, lambda is like an unnamed function for one simple use
# here the lambda function returns the first of 2 elements
def carLambda(pair):
    return pair(lambda a,b: a)
# here the lambda function returns the last of 2 elements
def cdrLambda(pair):
    return pair(lambda a,b: b)

assert carLambda(cons(3, 4)) == 3
assert cdrLambda(cons(3, 4)) == 4

# instead of a lambda its possible to go with nested functions
def car(pair):
    def first(a,b):
        return a
    return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    return pair(last)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4

# or even "regular/normal" functions
def firstNormal(a, b):
    return a
def lastNormal(a, b):
    return b
def carNormal(pair):
    return pair(firstNormal)
def cdrNormal(pair):
    return pair(lastNormal)

assert carNormal(cons(3, 4)) == 3
assert cdrNormal(cons(3, 4)) == 4

# this one took around 40 minutes, most of the time trying to understand WTF was that f(a,b)
# wouldnt get this solution on paper, need some prints and many try and error to remember all the basics

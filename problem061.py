# Problem #61 [Medium]
# Implement integer exponentiation. That is, implement the pow(x, y) function,
# where x and y are integers and returns x^y.
#
# Do this faster than the naive method of repeated multiplication.
#
# For example, pow(2, 10) should return 1024.


# the basic idea is to reduce the y value in every iteration until it gets to 0
def exponential(x, y):
    # when y gets to 0, the answer is always 1
    if y == 0:
        return 1

    # if y is negative, exponential is 1/x**abs(y)
    if y < 0:
        return 1 / exponential(x, abs(y))

    # if y is odd, multiply x one time by the exponential of x, y-1
    if y % 2 == 1:
        return x * exponential(x, y - 1)

    # this is the heart of this function, if y is even do pow(x,y/2) * pow(x,y/2), cutting the number of operations
    if y % 2 == 0:
        half_pow = exponential(x, y/2)
        return half_pow * half_pow


assert exponential(2, 0) == 1
assert exponential(0, 2) == 0
assert exponential(2, 1) == 2
assert exponential(2, 2) == 4
assert exponential(2, 3) == 8
assert exponential(2, 10) == 1024
assert exponential(2, 11) == 2048
assert exponential(-2, 1) == -2
assert exponential(-2, 2) == 4
assert exponential(-2, 3) == -8
assert exponential(-2, 4) == 16
assert exponential(2, -2) == 1/4
assert exponential(2, -3) == 1/8

# cool problem, i never thought about exponential on this way, for me it was always successive multiplication.
# took almost 1 hour to understand and get all possibilities

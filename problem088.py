# Problem #88
# Implement division of two positive integers without using the division, multiplication, or modulus operators.
# Return the quotient as an integer, ignoring the remainder.


def division(dividend, divisor):
    if divisor == 0:
        return None

    quotient = 0
    count = 0

    # sum divisor as many times is possible to put until it is less or equals to dividend
    while count + divisor <= dividend:
        quotient += 1
        count += divisor

    return quotient


assert division(1, 1) == 1
assert division(10, 0) is None
assert division(0, 10) == 0
assert division(5, 1) == 5
assert division(10, 5) == 2
assert division(10, 3) == 3
assert division(10, 9) == 1

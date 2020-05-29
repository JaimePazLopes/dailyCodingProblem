# Problem #85
# Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0,
# using only mathematical or bit operations. You can assume b can only be 1 or 0.


def if_b(x, y, b):
    if -b >> 1:
        return x
    return y


assert if_b(1, 2, 1) == 1
assert if_b(1, 2, 0) == 2
assert if_b(2, 1, 1) == 2
assert if_b(2, 1, 0) == 1

# using mathematical operations would be too easy for me because i am used to it but i am not used to use bit
# operations. did some tests and found this solution

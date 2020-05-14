# Problem #70 [Easy]
# A number is considered perfect if its digits sum up to exactly 10.
#
# Given a positive integer n, return the n-th perfect number.
#
# For example, given 1, you should return 19. Given 2, you should return 28.

import math


# i didnt know which was the best way to sum all digits, so i found this one on google. my first idea was transform in
# string, but i knew that couldnt be the best solution
def sum_digits(number):
    sum_ = 0
    while number:
        # get the less significant digit
        sum_ += number % 10
        # remove the less significant digit
        number //= 10
    return sum_


def perfect_number(n: int) -> int:
    if n <= 0:
        return 0

    n_count = 0
    number = 0

    # while you still dont have get to n
    while n != n_count:
        # go number by number
        number += 1
        # summ the digits
        perfect = sum_digits(number)
        # if it is perfect
        if perfect == 10:
            # add to the n count
            n_count += 1
    # when the ncount get to n, return number
    return number


assert (perfect_number(-1)) == 0
assert (perfect_number(0)) == 0
assert (perfect_number(1)) == 19
assert (perfect_number(2)) == 28


# formula that i found on https://www.geeksforgeeks.org/n-th-number-whose-sum-of-digits-is-ten/
def findNth(n):
    nthElement = 19 + (n - 1) * 9
    outliersCount = int(math.log10(nthElement)) - 1

    # find the nth perfect number
    nthElement += 9 * outliersCount
    return nthElement


assert (findNth(1)) == 19
assert (findNth(2)) == 28

# it was really quick to get to the first solution, just go number by number and get the n perfect number.
# i imagined that it was possible to get the answer using a formula, i tried without success to thing in one.
# after i google and found one in https://www.geeksforgeeks.org/n-th-number-whose-sum-of-digits-is-ten/. took around
# 45 minutes, most time trying to get to the formula

# Problem #67 [Medium]
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
#
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
#
# You can assume the list has at least three integers.


def largest_product(numbers: list) -> int:

    # copy and order the list
    numbers_copy = numbers.copy()
    numbers_copy.sort()

    # the the two smallest numbers and the biggest one, the two smallest might be big negative and become a big positive
    product_left = numbers_copy[0] * numbers_copy[1] * numbers_copy[-1]
    # take the 3 biggest numbers
    product_right = numbers_copy[-1] * numbers_copy[-2] * numbers_copy[-3]

    # return the biggest of them
    return max(product_left, product_right)


assert (largest_product([-10, -10, 5, 2])) == 500
assert (largest_product([-10, 10, 5, 2])) == 100
assert (largest_product([-10, -10, 5, 0])) == 500
assert (largest_product([-10, -10, -5, -2])) == -100

# i think that this can be done in a better way, but i am satisfied with nlogn. took around 30 minutes to notice the 2
# multiplications need, but to code was ridiculous quick.

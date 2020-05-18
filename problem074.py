# Problem #74 [Medium]
# Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and
# j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).
#
# Given integers N and X, write a function that returns the number of times X appears as a value in an N by N
# multiplication table.
#
# For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:
#
# | 1 |  2 |  3 |  4 |  5 |  6 |
# | 2 |  4 |  6 |  8 | 10 | 12 |
# | 3 |  6 |  9 | 12 | 15 | 18 |
# | 4 |  8 | 12 | 16 | 20 | 24 |
# | 5 | 10 | 15 | 20 | 25 | 30 |
# | 6 | 12 | 18 | 24 | 30 | 36 |
#
# And there are 4 12's in the table.


def number_of_times(N: int, X: int) -> int:
    # create a list with all numbers in N
    numbers = [number for number in range(1, N + 1)]
    # number of times X was found
    times = 0
    # for every numbers
    for number in numbers:
        # get value where: number * value = X
        value = X / number
        # if the value is in numbers means that number and value are in the table and its product is X
        if value in numbers:
            # count the number of times it matched
            times += 1
    return times


assert (number_of_times(1, 1)) == 1
assert (number_of_times(1, 2)) == 0
assert (number_of_times(6, 12)) == 4
assert (number_of_times(6, 1)) == 1
assert (number_of_times(6, 2)) == 2
assert (number_of_times(6, 4)) == 3

# simple problem, took around 20 minutes

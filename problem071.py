# Problem #71 [Easy]
# Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
# implement a function rand5() that returns an integer from 1 to 5 (inclusive).

import random


def rand7():
    return random.randint(1, 7)


def rand5():
    # get a rand7
    try_rand5 = rand7()
    # while it wont fit a rand5, keep getting new rand7
    while try_rand5 >= 6:
        try_rand5 = rand7()
    return try_rand5


# just counting each appearance of a value in an array
def count_values(array):
    values = dict()
    for value in array:
        if value in values.keys():
            values[value] += 1
        else:
            values[value] = 1
    return values


array_of_5 = [rand5() for _ in range(100000)]
print(count_values(array_of_5))

array_of_5 = [rand5() for _ in range(100000)]
print(count_values(array_of_5))

# really didnt understood the point of this one, its too similar to an old problem, but this one is made easier,
# instead of harder or at least different. took 5 minutes to do

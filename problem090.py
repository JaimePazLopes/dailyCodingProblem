# Problem #90
# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that
# isn't in l (uniform).

import random


def random_integer(n: int, l: list) -> int:

    random_n = random.randint(0, n-1)

    while random_n in l:
        random_n = random.randint(0, n - 1)

    return random_n


print(random_integer(10, []))
print(random_integer(10, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


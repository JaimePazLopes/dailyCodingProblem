# Problem #124
#
# You have 100 fair coins and you flip them all at the same time. Any that come up tails you set aside.
# The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?
#
# Write a function that, given $n$, returns the number of rounds you'd expect to play until one coin remains.

import math


def rounds_to_1_coin(n):
    if n <= 0:
        return None

    return math.ceil(math.log(n, 2))


print(rounds_to_1_coin(0))
print(rounds_to_1_coin(1))
print(rounds_to_1_coin(2))
print(rounds_to_1_coin(4))
print(rounds_to_1_coin(10))
print(rounds_to_1_coin(100))

# first i tried to go with successive divisions by 2, them i notice that log would be perfect for that. but i needed to
# google the round up function

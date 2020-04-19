# Problem #45[Easy]
# Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
# implement a function rand7() that returns an integer from 1 to 7 (inclusive).

import random


def rand5():
    return random.randint(1, 5)


def rand7():
    # get 2 random5, order matter
    first_5 = rand5()
    second_5 = rand5()

    # creating a dictionary with the correct distribution
    possible_7 = dict()
    # value will be between 1 and 7, and be added as values in the dict
    value = 0
    # this variable controls the number of possible values to be randomized, on the problem case 7
    # since i hardcoded only 2 rand5 together, this value can go until 25
    size = 7
    # this populate the dictionary
    for first in range(1, 6):
        for second in range(1, 6):
            value += 1
            # creating keys like: 11, 12, 13, 14, 15, 21, 22... and assigning value to them
            possible_7[str(first)+str(second)] = value
            # if the size is reached break the inner loop
            if value == size:
                break
        else:
            # if the inner loop finished, continue on the outer loop
            continue
        # to get here the else of the inner loop was not reached, that means that the break was reached on the
        # inner loop, so break outer loop
        break

    # if there is a key of the first random 5 + second random five, take it and return, if there isnt get new random
    while str(first_5)+str(second_5) not in possible_7.keys():
        first_5 = rand5()
        second_5 = rand5()
    return possible_7[str(first_5)+str(second_5)]


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

array_of_7 = [rand7() for _ in range(100000)]
print(count_values(array_of_7))


# i googled to find this solution using rejection sampling, this is quite specific for this case
def rand7_reject_specific():
    rand_max = 5 * (rand5() - 1) + rand5()
    while rand_max >= 22:
        rand_max = 5 * (rand5() - 1) + rand5()
    return (rand_max % 7) + 1


array_of_7 = [rand7_reject_specific() for _ in range(100000)]
print(count_values(array_of_7))


# i made it a little more generic to understand better how to use it
def rand_reject_generic(needed_rand=7, using_rand=5):

    # this formula has a equal distribution between 1 and 25, so the max need_rand is 25. but its possible to add
    # pow(using.rand,2) * (rand5() - 1) to need_rand go until 125, since you would add another part in the formula, the
    # max_random_value would be pow(using_rand,3)
    rand_max = using_rand * (random.randint(1, using_rand) - 1) + random.randint(1, using_rand)
    max_random_value = pow(using_rand, 2)  # 25 on this case

    # the multiplier its the number of times that needed_rand can be put in max_random_value
    multiplier = max_random_value // needed_rand  # 3 on this case
    # (needed_rand * multiplier) + 1 is where the rejection is made
    while rand_max >= (needed_rand * multiplier) + 1:  # 22 on this case
        # if it was reject, get a new random
        rand_max = using_rand * (random.randint(1, using_rand) - 1) + random.randint(1, using_rand)
    # take the modulus +1 to get value between 1 and 7
    return (rand_max % needed_rand) + 1


array_of_7 = [rand_reject_generic() for _ in range(100000)]
print(count_values(array_of_7))


# nice problem, i took some time trying to find a formula to make multiple rand5 create one rand7, but i saw that if i
# try to get a formula specific to that solution, i might need another one if I need rand8 or rand10. So I start to
# think in a more general method, so i get a dictionary solution. add in a dictionary one entry for each possible
# value making the keys be random numbers from rand5. I hardcoded a sequence of 2 rand5, making a dict of max size 25,
# more than enough for the 7 that the problem asked for. But the idea can be extended getting 3 rand5, going to 125
# possibilities. There is a cost to save those dicts and many rand5 will be randomized multiple times, but a solution
# with a bigger use satisfy me more.
# instead of thinking in the formula i googled it and found Rejection sampling, and the formula is quite generic and can
# fit well multiple cases
# finished in 30 40 minutes to my solution then another 30 40 minutes more to understand rejection sampling

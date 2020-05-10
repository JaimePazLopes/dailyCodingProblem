# Problem #66 [Medium]
# Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50
# (but also not 0-100 or 100-0). You do not know the bias of the coin.
# #
# # Write a function to simulate an unbiased coin toss.

from random import random


# based on the random_bias get a random coin flip
def toss_biased():
    random_number = random()
    if random_number <= random_bias:
        return 0
    return 1


# Used what I learned on this video https://www.youtube.com/watch?v=LIK0KqwKYXs
# toss 2 coin and ignore the same value, and 1 0 has the same chance as 0 1
def toss_unbiased():
    # try until get 2 different toss
    while True:
        # toss one time
        first_value = toss_biased()
        # toss another time
        second_value = toss_biased()
        # if they are different
        if second_value != first_value:
            # return the first one
            return first_value


for try_count in range(5):
    # create a coin probability
    random_bias = random()
    print("Try: ", try_count+1)
    print("Probability: ", random_bias)
    biased = {1: 0, 0: 0}
    unbiased = {1: 0, 0: 0}
    # throw the coin many times to get and idea of the distribution
    for i in range(100000):
        biased[toss_biased()] += 1
        unbiased[toss_unbiased()] += 1
    print(biased)
    print("Unbiased: ")
    print(unbiased)
    print()


# i didnt know how to start this one, did some tests but couldnt get a solution. had to google and found a video
# explaining how to do it, after that took some minutes to get the solution. took me around 45 minutes to finish

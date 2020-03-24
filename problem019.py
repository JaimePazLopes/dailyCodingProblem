# Problem #19 [Medium]
# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
# while ensuring that no two neighboring houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
# return the minimum cost which achieves this goal.

import numpy
# since I am studying numpy, I prefer use it directly
# create a group of random numbers for the painting costs, the costs will be between 10 and 20
#  3 is the color options and 5 are the number of houses, this will make the array[2][4] be the color 3 for the house 5
NK = numpy.random.randint(10, 20+1, (3, 5))
print(NK)

def minimumCost(NK, n=0, k=-1):
    minCost = -1
    # if there is no more houses return
    if n >= len(NK[0]):
        return 0
    # for each color
    for i in range(len(NK[:,0])):
        # if this color is different from the previous color
        if i == k:
            continue
        # get its cost + the cost of all future houses
        cost = NK[i][n] + minimumCost(NK, n+1, i)
        # if this cost is smaller than my smaller cost or there is no smaller cost, if becomes the smaller cost
        if cost < minCost or minCost < 0:
            minCost = cost
    return minCost

print(minimumCost(NK))

# the problem is easy, but i got really confused multiple times about which position is the color and the house
# took around 1 hour to finish


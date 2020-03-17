# Problem #12 [Hard]
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
# that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
    # 1, 1, 1, 1
    # 2, 1, 1
    # 1, 2, 1
    # 1, 1, 2
    # 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
# integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

steps = {1,2}
stairSize = 4
steps2 = {1,3,5}
stairSize2 = 5

# I think that in 12 problems I already did this function 3 times now, maybe 4. No secrets here, take every
# possibility of step each time trying to get to the end of the stair, if you get to the end, it is a solution
def uniqueWays(steps, stairSize):
    ways = []
    for step in steps:
        # ignore step backs or no step
        if step <= 0:
            continue
        # if the step is bigger than the stair, it is not an answer
        if step > stairSize:
            continue
        # if the step gets to the end of the stair, it is a solution
        if step == stairSize:
            ways.append(str(step))
            continue
        # if after the step there still stair, it keeps going
        if step < stairSize:
            temp = uniqueWays(steps, stairSize - step)
            for t in temp:
                ways.append(str(step) + str(t))

    return ways

uWays = uniqueWays([1], 1)
print(uWays, len(uWays))

uWays = uniqueWays([1], 0)
print(uWays, len(uWays))

uWays = uniqueWays([0], 1)
print(uWays, len(uWays))

uWays = uniqueWays(steps, stairSize)
print(uWays, len(uWays))

uWays = uniqueWays([1,2,3], stairSize)
print(uWays, len(uWays))

uWays = uniqueWays(steps, stairSize * 2)
print(uWays, len(uWays))

uWays = uniqueWays(steps2, stairSize2)
print(uWays, len(uWays))

uWays = uniqueWays(steps2, stairSize2*2)
print(uWays, len(uWays))

# easy problem, took for sure less than 30 minutes. This solution is so common that I will start to pay more
# attention to it, maybe more problems can be solved with something similar

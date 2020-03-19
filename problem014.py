# Problem #14 [Medium]
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x2 + y2 = r2.

# radius = 1, area of circle is only π
# considering the circle origin at 0,0, take multiple x,y values on the upper right corner (x and y between 0 and 1)
# this is 1/4 of the circle, so the area is π/4
# use x2 + y2 <= r2 to now if the point is inside the circle, x2 + y2 <= 1, because radius is 1

import random

# the bigger precision is the better the result is
def estimatePiMonteCarlo(precision):
    # points inside the circle
    insidePoints = 0
    for _ in range(precision):
        # creating random point
        point = [random.random(),random.random()]
        # checking if it is inside the circle
        if point[0]**2 + point[1]**2 <= 1:
            insidePoints += 1
    # estimate pi by dividing all points inside the circle for all the points in the group,
    # times * because its considering only a quarter of the circle
    return 4 * insidePoints / precision

print("{0:.3f}".format(estimatePiMonteCarlo(10)))
print("{0:.3f}".format(estimatePiMonteCarlo(100)))
print("{0:.3f}".format(estimatePiMonteCarlo(1000)))
print("{0:.3f}".format(estimatePiMonteCarlo(10000)))
print("{0:.3f}".format(estimatePiMonteCarlo(100000)))
print("{0:.3f}".format(estimatePiMonteCarlo(1000000)))
# print("{0:.3f}".format(estimatePiMonteCarlo(10000000)))

# I didnt know what the Monte Carlo method was, so I had to first google about it, after some minutes reading it a
# understood and was able to find a solution. dont remember how long I googled the method, but coding it was less then
# 10 minutes, did everythig is less then 30 minutes for sure

# Problem #30 [Medium]
# You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is
# unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
#
# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
#
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
#
# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth
# index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.


def filled(elevations):
    if len(elevations) <= 0:
        return 0

    # units of water filled
    water = 0
    # index for the actual hights
    leftIndex = 0
    rightIndex = len(elevations) - 1

    # highest wall on both sides
    leftHigh = rightHigh = 0

    # while the indexes are not the same
    while leftIndex - rightIndex != 0:
        # if the left side is bigger, work with the right side
        if elevations[leftIndex] > elevations[rightIndex]:
            # if the actual right elevation is bigger than the highest right elevation
            if elevations[rightIndex] > rightHigh:
                # highest right elevation = actual right elevation
                rightHigh = elevations[rightIndex]
            # if it is not, you can fill with water
            else:
                # fill with the difference between the highest elevation (side) - the actual elevation (bottom)
                water += rightHigh - elevations[rightIndex]
            # move the index to the left
            rightIndex -= 1
        # if the right side is bigger, work with the left side
        else:
            # if the actual left elevation is bigger than the highest left elevation
            if elevations[leftIndex] > leftHigh:
                # highest left elevation = actual left elevation
                leftHigh = elevations[leftIndex]
            # if it is not, you can fill with water
            else:
                # fill with the difference between the highest elevation (side) - the actual elevation (bottom)
                water += leftHigh - elevations[leftIndex]
            # move the index to the right
            leftIndex += 1
    return water


assert filled([2]) == 0
assert filled([]) == 0
assert filled([2, 1, 2]) == 1
assert filled([2, 2, 2]) == 0
assert filled([3, 0, 1, 3, 0, 5]) == 8
assert filled([4, 0, 1, 3, 0, 5]) == 12
assert filled([3, 0, 1, 3, 0, 0]) == 5

# could see the answer, i was trying to do going index by index, trying to find for the both sides of the area to fill
# and getting the lowest side * the distance between the sides - the sum of all bottoms, it was getting to weird and
# confused, so gave up. Looked online for this answer. Didnt even thought about attacking by both sides ath the same
# time. took me around of 1 hour and a half to do

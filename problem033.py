# Problem #33 [Easy]
#
# Compute the running median of a sequence of numbers. That is, given a stream of numbers,
# print out the median of the list so far on each new element.
#
# Recall that the median of an even-numbered list is the average of the two middle numbers.
#
# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
#
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2

import statistics
import heapq


sequence = [2, 1, 5, 7, 2, 0, 5]


# my first solution, looked online for a python way to do median
def running_median(sequence):
    for index in range(len(sequence)):
        print(statistics.median(sequence[:index+1]))
    print()


running_median(sequence)


# second solution, made my own median function
def median(sequence):
    sort = sorted(sequence)

    if len(sort) % 2 == 0:
        return (sort[int(len(sort)/2-1)] + sort[int(len(sort)/2)]) / 2
    else:
        return sort[int((len(sort)-1)/2)]


def running_median2(sequence):
    for index in range(len(sequence)):
        print(median(sequence[:index+1]))
    print()


running_median2(sequence)


# third solution, using min heap and max heap
def running_medians3(arr):
    if not arr:
        return None

    smallest_values = list()  # max heap of smallest values, multiply everything for -1 to get this effect
    biggest_values = list()  # min heap of biggest values

    for x in arr:
        # put it as a big value, so you can take the smallest value later
        heapq.heappush(biggest_values, x)
        # if they are no balanced, take one value of biggest to put on smallest
        if len(biggest_values) > len(smallest_values) + 1:
            # take the smallest element of the biggest values and add on the max heap of smallest values
            heapq.heappush(smallest_values, heapq.heappop(biggest_values) * -1)

        # if both have the same len
        if len(biggest_values) == len(smallest_values):
            # add the smallest element on biggest with the biggest element on smallest, divided by 2
            print((biggest_values[0] + (smallest_values[0] * -1)) / 2)
        else:
            # the middle element is the smallest element on biggest
            print(biggest_values[0])


running_medians3([2, 1, 5, 7, 2, 0, 5])

# the first 2 solution were easy and quick, but also quite bad. From the beginning i knew that i could do it in linear
# time, but to get there was hard, i got the idea of dividing on two parts but couldnt think in a way of keeping the
# lists ordered. Online I found heapq again, but it give only the smallest number, looking online for a max heap I
# found the * - 1 trick. It was not hard, but i didnt have to data structure know how. took one hour to finish

# Problem #95
#
# Given a number represented by a list of digits, find the next greater permutation of a number, in terms of
# lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest
# value/ordering.
#
# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1]
# should return [1,2,3].
#
# Can you perform the operation without allocating extra memory (disregarding the input memory)?

import itertools


def next_permutation(numbers):
    permutations = list(itertools.permutations(numbers))
    permutations.sort()

    index = permutations.index(tuple(numbers))
    index += 1
    if index == len(permutations):
        index = 0

    return list(permutations[index])


assert (next_permutation([1, 2, 3])) == [1, 3, 2]
assert (next_permutation([1, 3, 2])) == [2, 1, 3]
assert (next_permutation([2, 1, 3])) == [2, 3, 1]
assert (next_permutation([3, 2, 1])) == [1, 2, 3]


def next_permutation_2(numbers):

    # to get to this solutions i need to google

    # starting on the end, look for the first decreasing number
    i = len(numbers) - 2
    while i >= 0 and numbers[i + 1] <= numbers[i]:
        i -= 1

    # starting on the end, look for a number bigger than numbers[i] and swap it
    if i >= 0:
        j = len(numbers) - 1
        while j >= 0 and numbers[j] <= numbers[i]:
            j -= 1

        numbers[i], numbers[j] = numbers[j], numbers[i]

    # reverse the list after index i
    i += 1
    j = len(numbers) - 1
    while i < j:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1
        j -= 1

    return numbers


assert (next_permutation_2([1])) == [1]
assert (next_permutation_2([])) == []
assert (next_permutation_2([1, 2, 3])) == [1, 3, 2]
assert (next_permutation_2([1, 3, 2])) == [2, 1, 3]
assert (next_permutation_2([2, 1, 3])) == [2, 3, 1]
assert (next_permutation_2([3, 2, 1])) == [1, 2, 3]

# couldnt think in a solution by myself, i could do only the first function, but it is clearly far from what the problem
# asked for. try for around 30 minutes to get to something, but in the end i need to google for help. took around 1 hour
# 1 hour 15 to finish

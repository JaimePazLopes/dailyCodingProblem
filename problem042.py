# Problem #42 [Hard]
# Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
# If such a subset cannot be made, then return null.
#
# Integers can appear more than once in the list. You may assume all numbers in the list are positive.
#
# For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.


def subset_sum(array, k):
    # each time I do k-array[i], so when k==0 its over
    if k == 0:
        return []
    subset = []
    # for each index
    for i in range(len(array)):
        # create a new array that the element on this index dont exist
        new_array = array[:i] + array[i+1:]
        # try to put the actual element on the subset
        subset.append(array[i])
        # if the element is lower or equals to k, it can be used in the answer
        if array[i] <= k:
            # try to get a sum with the new array, and k-element
            result = subset_sum(new_array, k-array[i])
            # if didnt got a sum, take the element from subset and keep trying
            if result is None:
                subset.pop()
                continue
            else:
                # if found the sum add it to subset
                return subset + result
        # take it out of the subset
        subset.pop()


assert set(subset_sum([12, 1, 61, 5, 9, 2], 24)) == set([12, 9, 2, 1])
assert set(subset_sum([12, 1, 61, 5, 9, 2], 64)) == set([61, 2, 1])
assert subset_sum([12, 1, 61, 5, 9, 2], 4) is None
assert set(subset_sum([2, 2, 2, 2, 2, 2, 2, 2], 8)) == set([2, 2, 2, 2])

# easy problem but I got lost in the recursion, tried for around 30 40 minutes without success, stopped for a time and
# rewrite everything, this time finishing in 10 15 minutes. everything took me less than one hour

# Problem #60 [Medium]
# Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
#
# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true,
# since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.
#
# Given the multiset {15, 5, 20, 10, 35}, it would return false,
# since we can't split it up into two subsets that add up to the same sum.

from collections import Counter


# exists just to prepare the data for the actual method
def can_be_partitioned(multiset):
    # transform the list in a counter
    multiset = Counter(multiset)
    # create the multiset used to keep the values
    first_multiset = Counter()
    # call the actual method
    return _can_be_partitioned(multiset, first_multiset)


def _can_be_partitioned(multiset, first_multiset):
    # get the difference between all the values, and the values already stored
    missing_multiset = multiset - first_multiset
    # for each of those values
    for value in missing_multiset:
        # add it to the multiset
        first_multiset.update([value])
        # and get the difference between all the values and the updated multiset keeping the values
        second_multiset = multiset - first_multiset
        # if they have the same sum, return true
        if sum(first_multiset) == sum(second_multiset):
            return True
        # check the partition with the updated multiset
        if _can_be_partitioned(multiset, first_multiset):
            return True
        # if it was not possible to find a solution with the value, remove it
        first_multiset.subtract([value])
    # if no solution was found so far, there is no solution to found
    return False


assert not can_be_partitioned([])
assert not can_be_partitioned([1])
assert can_be_partitioned([15, 15])
assert can_be_partitioned([15, 5, 20, 10, 35, 15, 10])
assert not can_be_partitioned([15, 5, 20, 10, 35])

# i started doing with regular list, but quickly i realised that to put my idea on code would be necessary some weird
# operations to subtract on lists, decided to google for a multiset in python and found Counter. took 30 min to solve

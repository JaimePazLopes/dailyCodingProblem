# Problem #75 [Hard]
# Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does
# not necessarily have to be contiguous.
#
# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
# subsequence has length 6: it is 0, 2, 6, 9, 11, 15.


def longest_sequence(array: list, actual_index: int = 0, cache: dict = None) -> int:
    if actual_index >= len(array):
        return 0

    # save the count based on it index
    if cache is None:
        cache = dict()

    actual_value = array[actual_index]
    longest = 1
    # for all other next indexes
    for index in range(actual_index + 1, len(array)):
        # if they increase
        if array[index] >= actual_value:
            if index in cache:
                count = cache[index]
            else:
                # 1 for the actual + get the longest from this point
                count = 1 + longest_sequence(array, index, cache)
                cache[index] = count
            # check for longest
            if count > longest:
                longest = count

    return longest


assert (longest_sequence([])) == 0
assert (longest_sequence([1])) == 1
assert (longest_sequence([1, 2, 3, 4, 5])) == 5
assert (longest_sequence([1, 10, 3, 0, 5])) == 3
assert (longest_sequence([5, 4, 3, 2, 1])) == 1
assert (longest_sequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])) == 6

# i got a lot of problems on this, at first i tried doing using iteration, then i went for recursion, but was not able
# to get it. need to google to found this cache to save the counts. 1 hour to do everything

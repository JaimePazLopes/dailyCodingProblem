# Problem #49 [Medium]
# # Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# #
# # For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
# since we would take elements 42, 14, -5, and 86.
# #
# # Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
# #
# # Do this in O(N) time.


def max_sum(array):
    total_sum = 0
    if not array or len(array) <= 1:
        return total_sum
    actual_sum = 0
    # for each number
    for number in array:
        # add it to actual sum
        actual_sum += number

        # actual sum cant be negative
        if actual_sum < 0:
            actual_sum = 0

        # if actual sum is bigger than total sum, it becames total sum
        if actual_sum > total_sum:
            total_sum = actual_sum

    return total_sum


assert max_sum([]) == 0
assert max_sum([1]) == 0
assert max_sum([-5, -1, -8, -9]) == 0
assert max_sum([34, -50, 42, 14, -5, 86]) == 137
assert max_sum([34, -50, 42, 14, -5, 86, -200, 1, 2, 3]) == 137

# really simple problem, did in 10 minutes

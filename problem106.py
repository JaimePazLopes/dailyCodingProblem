# Problem #106
# Given an integer list where each number represents the number of hops you can make,
# determine whether you can reach to the last index starting at index 0.
#
# For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.


def is_end_reached(numbers):
    index = 0
    last_index = -1

    # while the index still in the array and the index keep changing
    while 0 <= index < len(numbers) - 1 and index != last_index:
        last_index = index
        # hop, add the value to index
        index += numbers[index]

    # if index is the last element, True, else, False
    return index == len(numbers) - 1


assert not (is_end_reached([]))
assert (is_end_reached([0]))
assert (is_end_reached([1]))
assert not (is_end_reached([0, 0]))
assert not (is_end_reached([2, 0]))
assert not (is_end_reached([-3, 0]))
assert (is_end_reached([2, 0, 1, 0]))
assert (is_end_reached([2, 2, -1, 0]))
assert not (is_end_reached([2, 0, 2, 0]))
assert not (is_end_reached([1, 1, 0, 1]))
assert (is_end_reached([1, 1, 1, 1]))

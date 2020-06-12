# Problem #99
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
# Return its length: 4.
#
# Your algorithm should run in O(n) complexity.


def get_longest_nlogn(numbers: list):

    numbers.sort()

    longest = 0
    count = 1

    for index in range(1, len(numbers)):
        # if the previous number ++ is equal to the actual number, they are in sequence, so count and continue
        if numbers[index - 1] + 1 == numbers[index]:
            count += 1
        # if they are not, restart the counting
        else:
            count = 1

        longest = max(longest, count)

    return longest


assert (get_longest_nlogn([])) == 0
assert (get_longest_nlogn([100, 4, 200, 1, 3, 2])) == 4
assert (get_longest_nlogn([100, 4, 200, 1, 3, 2, 5, 7, 6])) == 7
assert (get_longest_nlogn([100, 4, 200, 1, 3, 2, 13, 5, 33, 7, 6])) == 7
assert (get_longest_nlogn([100, 4, 200, 1, 2])) == 2


def get_longest_n(numbers: list):

    longest = 0

    # set is hash, in operation is O(1)
    uniques = set(numbers)

    for index in range(len(numbers)):

        # if there is no number previous then the actual, the actual number is a start of a sequence
        actual_number = numbers[index]
        if actual_number - 1 not in uniques:

            next_number = actual_number

            # look for the last number in sequence
            while next_number in uniques:
                next_number += 1
            
            sequence_size = next_number - actual_number
            longest = max(longest, sequence_size)

    return longest


assert (get_longest_n([])) == 0
assert (get_longest_n([100, 4, 200, 1, 3, 2])) == 4
assert (get_longest_n([100, 4, 200, 1, 3, 2, 5, 7, 6])) == 7
assert (get_longest_n([100, 4, 200, 1, 3, 2, 13, 5, 33, 7, 6])) == 7
assert (get_longest_n([100, 4, 200, 1, 2])) == 2

# my first idea was to order the array and them easily get the longest sequence, that solution is simple and nlogn.
# i couldnt get to a N solution, so i google it

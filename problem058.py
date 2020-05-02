# Problem #58 [Medium]
# An sorted array of integers was rotated an unknown number of times.
#
# Given such an array, find the index of the element in the array in faster than linear time.
# If the element doesn't exist in the array, return null.
#
# For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).
#
# You can assume all the integers in the array are unique.


def find_index(array, element, start=0, end=None):
    if end is None:
        end = len(array) - 1

    # the element is not in the array
    if start > end:
        return None

    # check if the array middle is the element
    middle = (start + end) // 2
    if array[middle] == element:
        return middle

    # the numbers in the first part are sorted
    if array[start] <= array[middle]:
        # and the element is in the first part
        if array[start] <= element <= array[middle]:
            # look for the element in the first part
            return find_index(array, element, start, middle-1)
        # look for the element in the second part
        return find_index(array, element, middle+1, end)
    # the numbers in the second part are sorted
    else:
        # and the element is in the second part
        if array[middle] <= element <= array[end]:
            # look for the element in the second part
            return find_index(array, element, middle+1, end)
        # look for the element in the first part
        return find_index(array, element, start, middle-1)


array = [13, 18, 25, 2, 8, 10]
for index in range(len(array)):
    assert find_index(array, array[index]) == index
assert find_index(array, 15) is None
assert find_index(array, 22) is None
assert find_index(array, 5) is None
assert find_index(array, 11) is None

# the problem seemed easy, i knew i have to use binary search and i need the first element and the middle to see with
# part of the array i need to check. I tried for a long time, maybe around 2 hours to do a recursive solution that keep
# getting the subarray that the element is in, but for some reason i couldnt got it right what part of the array to
# choose. Went online to find this solution of not getting the subarray itself, but passing the index of the subarray

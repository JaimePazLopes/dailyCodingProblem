# Problem #44 [Medium]
# We can determine how "out of order" an array A is by counting the number of inversions it has.
# Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after
# a larger element.
#
# Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
#
# You may assume each element in the array is distinct.
#
# For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and
# (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


# the O(n²) is really simple, but not what the problem ask for
def inversions_n2(array):
    inversions = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] > array[j] and i < j:
                inversions += 1
    return inversions


assert inversions_n2([1, 2, 3, 4, 5]) == 0
assert inversions_n2([2, 4, 1, 3, 5]) == 3
assert inversions_n2([5, 4, 3, 2, 1]) == 10


# it is really simple to improve this solution, just seeing the if you can find a better one.
# There is a restriction there on if i < j, we can take this if restriction and put it on the for,
# making j always bigger than i. Reducing the time, but not the complexity, this still is n²
def inversions_n2_2(array):
    inversions = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                inversions += 1
    return inversions


assert inversions_n2_2([1, 2, 3, 4, 5]) == 0
assert inversions_n2_2([2, 4, 1, 3, 5]) == 3
assert inversions_n2_2([5, 4, 3, 2, 1]) == 10


# using the merge sort to count the inversions
def merge_inversions(array):
    if len(array) <= 1:
        return 0

    # divide the array in 2 parts
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    # get the number of inversions on both sides of the array
    left_inversions = merge_inversions(left)
    right_inversions = merge_inversions(right)

    left_index = right_index = array_index = actual_inversions = 0

    # iterate on the left side and right side getting always the smallest number and adding to the array
    # both sides get here already in the right order
    while left_index < len(left) and right_index < len(right):
        # if the smaller value is on the left, it is already "in order" so just copy it to the array
        if left[left_index] < right[right_index]:
            array[array_index] = left[left_index]
            left_index += 1
        # if the right is bigger, means "out of order", but when you copy it to the array, you are actually doing
        # "multiple inversions". this element is skipping all elements that still are on the left array
        else:
            array[array_index] = right[right_index]
            right_index += 1
            actual_inversions += len(left) - left_index
        array_index += 1

    # both "while" just finish copying any remaining element on left and right to the array
    while left_index < len(left):
        array[array_index] = left[left_index]
        left_index += 1
        array_index += 1

    while right_index < len(right):
        array[array_index] = right[right_index]
        right_index += 1
        array_index += 1

    return left_inversions + right_inversions + actual_inversions


assert merge_inversions([1, 2, 3, 4, 5]) == 0, merge_inversions([1, 2, 3, 4, 5])
assert merge_inversions([2, 4, 1, 3, 5]) == 3, merge_inversions([2, 4, 1, 3, 5])
assert merge_inversions([5, 4, 3, 2, 1]) == 10, merge_inversions([5, 4, 3, 2, 1])

# took not even 5 minutes to do both n² solutions, both that didnt help me to get to a better solution. It was clear
# that i need a sorting algorithm to do that, but i could remember how to code anyone that is better than n².
# looking online i choose merge sort, it is n log(n) and looks easier to understand. I copy the code from GeeksforGeeks
# and add the inversion counter. everything took a little more than 1 hour

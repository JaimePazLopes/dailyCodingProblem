# Problem #78
# Given an array of integers, write a function to determine whether the array could become non-decreasing by
# modifying at most 1 element.
#
# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make
# the array non-decreasing.
#
# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a
# non-decreasing array.


def could_become(numbers):
    # count how many changes are necessary
    modify = 0

    if not numbers:
        return False

    previous = numbers[0]

    # for each element
    for index in range(1, len(numbers)):
        # compare it with the previous one
        if previous > numbers[index]:
            # if it is bigger, it needs to be modified
            modify += 1
        previous = numbers[index]

    # if there is more than 1 modified number, its false
    return modify <= 1


assert (could_become([1, 2, 3]))
assert (could_become([1, 1, 1]))
assert (could_become([1, 1, 2]))
assert not (could_become([3, 2, 1]))
assert (could_become([3, 1, 2]))
assert (could_become([10, 5, 7]))
assert not (could_become([10, 5, 1]))

# simple problem, nothing special. did in less than 15 minutes

# Problem #102
#
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
#
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4].


def sublist_k(numbers: list, k: int) -> list:
    sublist = list()

    if k == 0:
        return sublist

    # for each number
    for number in numbers:

        # while the sum of the sublist + number is bigger than k, remove the first element of the sublist
        while sublist and sum(sublist) + number > k:
            del sublist[0]

        # add the new element
        sublist.append(number)

        # if the sum is equal to k, return it
        if sum(sublist) == k:
            return sublist

    return None


assert sublist_k([], 0) == []
assert sublist_k([], 1) is None
assert sublist_k([1, 2, 3, 4, 5], 0) == []
assert sublist_k([1, 2, 3, 4, 5], 2) == [2]
assert sublist_k([1, 2, 3, 4, 5], 3) == [1, 2]
assert sublist_k([1, 2, 3, 4, 5], 9) == [2, 3, 4]
assert sublist_k([5, 4, 3, 2, 1], 9) == [5, 4]
assert sublist_k([5, 4, 3, 2, 1], 6) == [3, 2, 1]
assert sublist_k([5, 4, 3, 2, 1], 12) == [5, 4, 3]
assert sublist_k([5, 4, -3, 2, 1], 1) == [4, -3]
assert sublist_k([1, -2, 3, 4, 5], -1) == [1, -2]

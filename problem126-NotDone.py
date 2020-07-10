# Problem #126
#
# Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes
# [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list.
# How many swap or move operations do you need?
#
# [1, 2, 3, 4, 5, 6]
# [5, 2, 3, 4, 1, 6]
# [5, 6, 3, 4, 1, 2]
# [3, 4, 5, 6, 1, 2]


def rotate_k(numbers, k):
    if not numbers:
        return None

    if k == 0:
        return numbers

    k = k % len(numbers)

    for index in range(len(numbers) - 1, -1, -1):
        numbers[index], numbers[index - k] = numbers[index - k], numbers[index]

    return numbers


print(rotate_k(None, 0))
print(rotate_k([], 2))
print(0, rotate_k([1, 2, 3, 4, 5, 6], 0))
print(1, rotate_k([1, 2, 3, 4, 5, 6], 1))
print(2, rotate_k([1, 2, 3, 4, 5, 6], 2))
print(3, rotate_k([1, 2, 3, 4, 5, 6], 3))
print(4, rotate_k([1, 2, 3, 4, 5, 6], 4))
print(5, rotate_k([1, 2, 3, 4, 5, 6], 5))
print(6, rotate_k([1, 2, 3, 4, 5, 6], 6))
print(8, rotate_k([1, 2, 3, 4, 5, 6], 8))

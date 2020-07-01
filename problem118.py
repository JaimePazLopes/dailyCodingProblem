# Problem #118
#
# Given a sorted list of integers, square the elements and give the output in sorted order.
#
# For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].


def square_list_simple(numbers: list):
    squared = numbers.copy()

    # square
    for index in range(len(squared)):
        squared[index] *= squared[index]

    # sort
    squared.sort()

    return squared


assert (square_list_simple([-9, -2, 0, 2, 3])) == [0, 4, 4, 9, 81]


def square_list(numbers: list):
    # make 2 lists, one for the negative numbers squared and other for the positive numbers squared
    negative_squared = list()
    positive_squared = list()

    # take all numbers and square it appending on the right list
    for index in range(len(numbers)):
        if numbers[index] < 0:
            negative_squared.append(numbers[index]**2)
        else:
            positive_squared.append(numbers[index]**2)

    # start the index, the positive list in sorted, the negative list is sorted
    positive_index = 0
    negative_index = len(negative_squared) - 1

    squared = list()

    # order the lists taking the lower values from each list
    while negative_index >= 0 and positive_index < len(positive_squared):
        if negative_squared[negative_index] <= positive_squared[positive_index]:
            squared.append(negative_squared[negative_index])
            negative_index -= 1
        else:
            squared.append((positive_squared[positive_index]))
            positive_index += 1

    # in case there is elements in one of those lists, extend it to the squared list
    if negative_index >= 0:
        squared.extend(reversed(negative_squared[:negative_index + 1]))
    else:
        squared.extend(positive_squared[positive_index:])

    return squared


assert (square_list([])) == []
assert (square_list([1])) == [1]
assert (square_list([-1])) == [1]
assert (square_list([-9, -2, 0, 2, 3])) == [0, 4, 4, 9, 81]
assert (square_list([-9, -2])) == [4, 81]
assert (square_list([0, 2, 3])) == [0, 4, 9]
assert (square_list([0, 1, 2, 3, 5, 10])) == [0, 1, 4, 9, 25, 100]
assert (square_list([-3, -2, -1, 0, 1, 2, 3, 5, 10])) == [0, 1, 1, 4, 4, 9, 9, 25, 100]
assert (square_list([-20, -13, -11, -3, -2, -1, 0, 1, 2, 3, 5, 10])) == [0, 1, 1, 4, 4, 9, 9, 25, 100, 121, 169, 400]

# first i did the easy way, just square everything and call sort. after i decided to go with a more polished solution.

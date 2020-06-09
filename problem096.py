# Problem #96
#
# Given a number in the form of a list of digits, return all possible permutations.
#
# For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].


import itertools


def auto_permutations(numbers):
    return list(itertools.permutations(numbers))


def permutations(numbers):

    all_permutations = list()

    # if it is one element or less, return it as the only permutation
    if len(numbers) <= 1:
        all_permutations.append(numbers)
        return all_permutations

    # for each elements
    for i in range(len(numbers)):
        number = numbers[i]
        # make a new list without it
        partials = numbers.copy()
        del partials[i]
        # all get all permutations of it
        new_permutations = permutations(partials)

        # combine the new permutations with the removed element
        for new in new_permutations:
            new.insert(0, number)
            all_permutations.append(new)

    return all_permutations


print(auto_permutations([1, 2, 3]))
print(permutations([1, 2, 3]))


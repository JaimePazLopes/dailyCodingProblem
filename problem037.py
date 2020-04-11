# Problem #37 [Easy]
# The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
#
# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
#
# You may also use a list or array to represent a set.


def get_power_set(given_set):
    # create an empty list
    power_set = []
    # if the given list is empty
    if len(given_set) == 0:
        # add the empty set to the power set and return it
        power_set.append([])
        return power_set

    # the logic on the problem is, take one of the element, get all the subsets without it, and then add it to all
    # subsets
    # I take the last element to try to put in a better order, in the end i decided to call a sorted to do it
    actual_element = given_set[-1]
    # make all subsets without it
    subsets = get_power_set(given_set[:-1])
    # add them to the power set
    power_set.extend(subsets)

    # add the remove element to all subsets
    for subset in subsets:
        # copy, always remember to copy, this always make me trouble
        adding_set = subset.copy()
        # add the element to the subset
        adding_set.append(actual_element)
        # add it to the power set
        power_set.append(adding_set)

    # sorting to be easy to check the answer
    return sorted(power_set, key=len)


print(get_power_set([]))
print(get_power_set([1]))
print(get_power_set([1, 2]))
print(get_power_set([1, 2, 3]))
print(get_power_set([1, 2, 3, 4]))
print(get_power_set([1, 2, 3, 4, 5]))

# the problem was easy, what made me lost a lot of time was trying to solve it with set, dont know if it is possible or
# how to do it, i tried and i failed. with lists was quick. took me 15 min. but i put more than one hour trying to do
# it as set

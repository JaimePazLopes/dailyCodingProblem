# Problem #86
# Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make
# the string valid (i.e. each open parenthesis is eventually closed).
#
# For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we
# must remove all of them.


def parentheses_to_remove(sequence):
    # number of parentheses to remove
    count = 0
    # number of parentheses already open
    opened = 0

    # for each char in the sequence
    for char in sequence:
        # if it is opening, add it to the opened count
        if char == "(":
            opened += 1
        # if it is closing
        if char == ")":
            # and there is opened parentheses, close it by removing it of the opened count
            if opened > 0:
                opened -= 1
            # if there is no open parentheses, add the number of parentheses to remove
            else:
                count += 1

    # return the number of parentheses to remove + the number of opened parentheses not closed
    return count + opened


assert (parentheses_to_remove("")) == 0
assert (parentheses_to_remove("()")) == 0
assert (parentheses_to_remove("()())()")) == 1
assert (parentheses_to_remove("()()()()")) == 0
assert (parentheses_to_remove(")(")) == 2
assert (parentheses_to_remove("(((")) == 3
assert (parentheses_to_remove(")))")) == 3
assert (parentheses_to_remove(")))")) == 3
assert (parentheses_to_remove("stuff)in)the)middle")) == 3

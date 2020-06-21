# Problem #108
#
# Given two strings A and B, return whether or not A can be shifted some number of times to get B.
#
# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.


def can_be_shift(A, B):
    if not A or not B:
        return False

    # I make all the shifts and check if in any of them it becomes equals to B
    for index in range(len(A)):
        if A[index:] + A[:index] == B:
            return True
    return False


assert not (can_be_shift("", ""))
assert not (can_be_shift(None, None))
assert (can_be_shift("abcde", "cdeab"))
assert not (can_be_shift("abc", "acb"))

# Problem #121
#
# Given a string which we can delete at most k, return whether you can make a palindrome.
#
# For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.


def can_make_palindrome(word, k):
    if word is None:
        return False
    if k == 0:
        return word == word[::-1]

    # seting the variables
    working_k = k
    front_index = 0
    back_index = len(word) - 1
    one_side = True

    # iterate over the both sides of the array at the same time
    while front_index <= back_index:
        # if a match was found, go to next indexes
        if word[front_index] == word[back_index]:
            front_index += 1
            back_index -= 1
            continue

        # if no match was found, count it on k, and move only one index. if there is no more k, there is no solution
        working_k -= 1
        back_index -= 1
        if working_k < 0:
            one_side = False
            break

    # them i do the same thing again, but instead of skipping the back when no match is found, I skip the front
    working_k = k
    front_index = 0
    back_index = len(word) - 1
    other_side = True

    while front_index <= back_index:

        if word[front_index] == word[back_index]:
            front_index += 1
            back_index -= 1
            continue

        working_k -= 1
        front_index += 1
        if working_k < 0:
            other_side = False
            break

    # if it was a match in front or in the back, return true
    return one_side or other_side


assert (can_make_palindrome('', 0))
assert (can_make_palindrome('a', 0))
assert (can_make_palindrome('aaa', 0))
assert (can_make_palindrome('aba', 0))
assert not (can_make_palindrome('abca', 0))
assert (can_make_palindrome('abca', 1))
assert (can_make_palindrome('abca', 10))

assert not (can_make_palindrome('waterrfetawx', 0))
assert not (can_make_palindrome('waterrfetawx', 1))
assert (can_make_palindrome('waterrfetawx', 2))
assert (can_make_palindrome('waterrfetawx', 3))

assert not (can_make_palindrome('xwatefrretaw', 0))
assert not (can_make_palindrome('xwatefrretaw', 1))
assert (can_make_palindrome('xwatefrretaw', 2))
assert (can_make_palindrome('xwatefrretaw', 3))

# this problem looks perfect for recursion, but most problems use recursion as a easier solution, so i tried to solve
# it without it. i got a okish solution, i didnt like that i needed to while to complete it.

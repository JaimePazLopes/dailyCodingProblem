# Problem #31 [Easy]
# The edit distance between two strings refers to the minimum number of character insertions, deletions,
# and substitutions required to change one string to the other. For example, the edit distance between “kitten” and
# “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
#
# Given two strings, compute the edit distance between them.


def editDistance(string1, string2):
    # if one of the strings is empty, the distance will be the other string len
    if string1 == "":
        return len(string2)
    if string2 == "":
        return len(string1)
    # if they are the same the distance is 0
    if string1 == string2:
        return 0

    # if the char on index 0 of both strings is the same, go to the next char
    if string1[0] == string2[0]:
        return editDistance(string1[1:], string2[1:])

    # test multiple possibilities:
    # skip left to simulate adding a char on string 1
    skipleft = 1 + editDistance(string1[1:], string2)
    # skip right to simulate adding a char on string 2
    skipright = 1 + editDistance(string1, string2[1:])
    # skip both to simulate different char
    skipboth = 1 + editDistance(string1[1:], string2[1:])
    # get the smallest distance
    minvalue = min(skipleft, skipright, skipboth)

    return minvalue


assert editDistance("", "") == 0
assert editDistance("a", "a") == 0
assert editDistance("a", "b") == 1
assert editDistance("qwerty", "qw") == 4
assert editDistance("qwerty", "") == 6
assert editDistance("kitten", "sitting") == 3
assert editDistance("banana", "panama") == 2
assert editDistance("banana", "panama") == 2
assert editDistance("banana", "anana") == 1

# easy problem, but with only one example, not even the worst case, i understood the problem wrong at first.

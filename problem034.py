# Problem #34 [Medium]
# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
# anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
# lexicographically earliest one (the first one alphabetically).
#
# For example, given the string "race", you should return "ecarace", since we can add three letters to it
# (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race"
# by adding three letters, but "ecarace" comes first alphabetically.
#
# As another example, given the string "google", you should return "elgoogle".


def create_palindrome(word):
    # if word is equal to its reverse, return it
    if word == word[::-1]:
        return word

    # if the first and last char are the same, try to make a palindrome with the middle "word"
    if word[0] == word[-1]:
        return word[0] + create_palindrome(word[1:-1]) + word[-1]
    # if they are not the same, make them the same
    else:
        # force the first char to be the last char too, try to make a palindrome with the middle "word"
        by_first = word[0] + create_palindrome(word[1:]) + word[0]
        # force the last char to be the first too, try to make a palindrome with the middle "word"
        by_last = word[-1] + create_palindrome(word[:-1]) + word[-1]

        # return the answer with less chars
        if len(by_first) > len(by_last):
            return by_last
        elif len(by_first) < len(by_last):
            return by_first

        # return the answer in alphabetic order
        if by_first < by_last:
            return by_first
        return by_last


assert create_palindrome("arara") == "arara"
assert create_palindrome("a") == "a"
assert create_palindrome("race") == "ecarace"
assert create_palindrome("google") == "elgoogle"

# it looked easy at first, but after finding my solution i read again the problem, it says "ANYWHERE in the word",
# i did for the beggining or ending only. couldnt think on a solution in time and looked for one online, it still a
# little weird will try to come back later

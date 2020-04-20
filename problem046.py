# Problem #46 [Hard]

# Given a string, find the longest palindromic contiguous substring.
# If there are more than one with the maximum length, return any one.
#
# For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
# The longest palindromic substring of "bananas" is "anana".


def longest_palindromic(word):
    if word == word[::-1]:
        return word

    without_first = longest_palindromic(word[1:])
    without_last = longest_palindromic(word[:-1])

    if len(without_first) > len(without_last):
        return without_first

    return without_last


print(longest_palindromic("aabcdcb"))
print(longest_palindromic("bananas"))
print(longest_palindromic(""))
print(longest_palindromic("a"))
print(longest_palindromic("abcde"))
print(longest_palindromic("abccccde"))
print(longest_palindromic("abcdeeee"))

# i think i understood something wrong here, they say that is a hard problem, but this is one of the easiest problem
# they sent. i finished in 5 minutes, but spent more 10 to be sure i was doing what i was supposed to do

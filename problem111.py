# Problem #111
#
# Given a word W and a string S, find all starting indices in S which are anagrams of W.
#
# For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

from collections import Counter


def find_all_anagrams(W, S):
    matches = []

    word_size = len(W)

    # starting on all index, take the word and a substring with same size to check for anagram
    for index in range(len(S) - word_size + 1):
        if is_anagram(W, S[index:index + word_size]):
            matches.append(index)

    return matches


# just a simple anagram check between two words
def is_anagram(word, substring):
    return Counter(word) == Counter(substring)


assert (find_all_anagrams("ab", "abxaba")) == [0, 3, 4]
assert (find_all_anagrams("banana", "nabanaan")) == [0, 2]

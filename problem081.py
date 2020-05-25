# Problem #81
# Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the
# number could represent. You can assume each valid number in the mapping is a single digit.
#
# For example if {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], } then "23" should return
# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
import itertools


def get_messages(digits, text):

    list_of_letters = list()

    # take all the lists of letters
    for char in text:
        letters = digits[char]
        list_of_letters.append(letters)

    # combine all of them
    combinations = list(itertools.product(*list_of_letters))

    messages = list()

    # transformer them into strings
    for combination in combinations:
        message = "".join(combination)
        messages.append(message)

    return messages


digits = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
    "0": [" "]
}

assert (get_messages(digits, "23")) == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
assert "banana" in (get_messages(digits, "226262"))
assert "a b c" in (get_messages(digits, "20202"))

# i think that using itertools is a little cheating on a problem like this, but since i use it more to practice python
# for me this a better solution. took me around 20~30 minutes

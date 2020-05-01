# Problem #57 [Medium]
# Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or
# less. You must break it up so that words don't break across lines. If there's no way to break the text up,
# then return null.
#
# You can assume that there are no spaces at the ends of the string and
# that there is exactly one space between each word.
#
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return:
# ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.


def break_text(text, k):
    # split the text on " "
    splits = text.split(" ")
    # see if any word is bigger than k, if at least one word is, it is not possible to break the text
    if k < len(max(splits, key=len)):
        return None
    broken = []
    # line is each broken part of the text
    line = splits[0]
    # for each split
    for split in splits[1:]:
        # if line + empty space + the split is smaller than k, you can put them together
        if len(line) + 1 + len(split) <= k:
            line += " " + split
        # if they are bigger, add the line to the list and restart the line with split
        else:
            broken.append(line)
            line = split
    # add the working line
    broken.append(line)
    return broken


message = "the quick brown fox jumps over the lazy dog"
assert break_text("asdasfaasfasfasfasfa", 10) is None
assert break_text(message, 10) == ["the quick", "brown fox", "jumps over", "the lazy", "dog"]
assert break_text(message, 12) == ["the quick", "brown fox", "jumps over", "the lazy dog"]
assert break_text(message, 6) == ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

# really simple and easy problem, took around 15 minutes

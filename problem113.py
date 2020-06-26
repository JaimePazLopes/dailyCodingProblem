# Problem #113
#
# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here",
# return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation in-place?


def reverse(message):
    return " ".join(message.split()[::-1])


print(reverse("hello world here"))
print(reverse("hello world here there"))

# tried to look for a way to do the follow-up. but couldnt find a good answer for how to make a mutable string
# representation

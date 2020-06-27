# Problem #114
#
# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the
# delimiters. For example, given "hello/world:here", return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"


def reverse(message, delimiters):
    split_message = message

    for delimiter in delimiters:
        split_message = split_message.replace(delimiter, " ")

    split_message = split_message.split()[::-1]

    return_message = ""

    for index in range(len(split_message)):
        return_message += split_message[index]
        if index < len(delimiters):
            return_message += delimiters[index]

    return return_message


print(reverse("hello/world:here", ["/", ":"]))
print(reverse("hello/world:here/", ["/", ":", "/"]))
print(reverse("hello//world:here", ["//", ":"]))

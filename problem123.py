# Problem #123
#
# Given a string, return whether it represents a number. Here are the different kinds of numbers:
#
#     "10", a positive integer
#     "-10", a negative integer
#     "10.1", a positive real number
#     "-10.1", a negative real number
#     "1e5", a number in scientific notation
#
# And here are examples of non-numbers:
#
#     "a"
#     "x 1"
#     "a -2"
#     "-"


def is_number(message):
    if not message:
        return False

    # take the - in front of the string
    if message[0] == "-":
        if len(message) == 1:
            return False
        message = message[1:]

    # if there is too many . e -, it is not a number
    if message.count(".") > 1 or message.count("e") > 1 or message.count("-") > 0:
        return False

    # break the string by removing the . e
    split_e = message.split("e")
    split_dot = split_e[0].split(".")

    # get all splits together
    if len(split_e) == 2:
        split_dot.extend(split_e[1])

    # go on each character of each split, if they are not a number, return false
    for s in split_dot:
        for character in s:
            if character not in "0123456789":
                return False

    return True


assert (is_number("10"))
assert (is_number("10.1"))
assert (is_number("10.0"))
assert (is_number("-10.1"))
assert (is_number("1e5"))
assert not (is_number("a"))
assert not (is_number("x 1"))
assert not (is_number("a -2"))
assert not (is_number("-"))
assert not (is_number("-10-"))
assert not (is_number("-10.10.10"))
assert not (is_number("-10e10e10"))

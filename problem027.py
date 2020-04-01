# Problem #27 [Easy]
# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced
# (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.


def isBalanced(message):
    # on this structure i append every opening and pop when i find the pairing closing
    structure = []
    # for each char
    for char in message:
        # if it is a opening, i append
        if char in "({[":
            structure.append(char)
        # if it is a closing and it's pairing opening is the last element on the structure i pop
        elif char == "}" and structure[-1] == "{":
            structure.pop()
        elif char == "]" and structure[-1] == "[":
            structure.pop()
        elif char == ")" and structure[-1] == "(":
            structure.pop()
        # if it is a closing without pair, return false
        elif char in "}])":
            return False
    # if there are elements on the structure return false
    if len(structure) != 0:
        return False
    return True


assert isBalanced("([])[]({})")
assert not isBalanced("([)]")
assert not isBalanced("((()")
assert isBalanced("")
assert isBalanced("()")
assert isBalanced("[]")
assert isBalanced("{}")
assert not isBalanced("[}")
assert isBalanced("(banana)")
assert isBalanced("print(min(2,3))")
assert not isBalanced("print(min(2,3)")

# really simple problem, took 15 min to do

# Problem  # 25 [Hard]
# Implement regular expression matching with the following special characters:
#
#     . (period) which matches any single character
#     * (asterisk) which matches zero or more of the preceding element
#
# That is, implement a function that takes in a string and a valid regular expression and returns whether or
# not the string matches the regular expression.
#
# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.
#
# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.


def isMatch(expression, message):
    messageIndex = 0
    expressionIndex = 0
    # if i check the whole expression or the whole message stop the iteration
    while expressionIndex < len(expression) and messageIndex < len(message):
        # take the actual expression and message char, and increment indexes
        expressionChar = expression[expressionIndex]
        messsageChar = message[messageIndex]
        expressionIndex += 1
        messageIndex += 1
        # if the expression is *
        if expressionChar == "*":
            # take the char before *
            expressionChar = expression[expressionIndex - 2]
            # take also a possible char after
            if expressionIndex < 0 or expressionIndex >= len(expression):
                nextexpressionChar = ""
            else:
                nextexpressionChar = expression[expressionIndex]
            messageIndex -= 2
            # keep getting the next char on message
            while messageIndex < len(message):
                messsageChar = message[messageIndex]
                # if you found on the message the next expression char, you stop looking
                if nextexpressionChar == messsageChar:
                    break
                # if you found a different char that is not ., return False
                if expressionChar != messsageChar and expressionChar != ".":
                    return False
                messageIndex += 1
        # if the chars are different and not . and not the char before a *, return False
        elif expressionChar != messsageChar and expressionChar != "." and expression[expressionIndex] != "*":
            return False
    # if there is still message, return false
    if messageIndex < len(message):
        return False
    # if there is still expression and it didnt finish with *, return false
    if expressionIndex < len(expression) and expression[-1] != "*":
        return False
    return True


assert isMatch("banana", "banana")
assert not isMatch("bana", "banana")
assert not isMatch("banana", "bana")
assert isMatch(".", "a")
assert not isMatch("*", "a")
assert isMatch("banana*", "banana")
assert isMatch("a*", "a")
assert isMatch(".*", "a")
assert isMatch("ra.", "ray")
assert not isMatch("ra.", "raymond")
assert isMatch("ra.*", "raymond")
assert isMatch(".*at", "chat")
assert isMatch(".*at", "at")
assert not isMatch(".*at", "chats")
assert isMatch(".*at.", "chats")
assert isMatch(".*at.*", "chats")
assert isMatch(".*banana", "banana")
assert isMatch("b*anana", "bbbbbbbbbbbbbbbanana")
assert not isMatch("b*anana", "bbbbbccccbbbbbbbbbbanana")
assert isMatch("b*anana", "anana")
assert not isMatch("b*anana", "canana")
assert isMatch("banana*", "bananaaaaaaaa")
assert isMatch("banc*ana*", "banana")
assert isMatch("banana*", "ba")

# took me around one hour, at first the idea of going char by char sounded really good. after finishing i think that
# a recursion solution would be much more simple.

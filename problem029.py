# Problem #29 [Easy]
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
# successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
# solely of alphabetic characters. You can assume the string to be decoded is valid.


def encode(message):
    # encoded message
    newmessage = ""
    # previous char to compare with actual char
    previouschar = ""
    # counting the same char
    countchar = 0
    # for each char in message
    for char in message:
        # if previous was assigned and previous is different from char
        if previouschar != "" and previouschar != char:
            # add the count and the previous char
            newmessage += str(countchar) + previouschar
            # restart the counting
            countchar = 0
        # count the char
        countchar += 1
        # set char as previous
        previouschar = char
    else:
        # add the last char to the encoded message
        newmessage += str(countchar) + previouschar
    return newmessage


def decode(message):
    # decoded message
    newmessage = ""
    # for each 2 values (remember that the encoded message is always a number of char and the char in succession)
    for i in range(0, len(message), 2):
        # take the char e repeat it the amount of times
        newmessage += message[i+1] * int(message[i])

    return newmessage


test = "AAAABBBCCDAA"
print(test)
print(encode(test))
print(decode(encode(test)))
print("")
test = "ABCDEFGHIJ"
print(test)
print(encode(test))
print(decode(encode(test)))
print("")
test = "BANANA"
print(test)
print(encode(test))
print(decode(encode(test)))
print("")
test = "ZZZ"
print(test)
print(encode(test))
print(decode(encode(test)))
print("")
test = "A"
print(test)
print(encode(test))
print(decode(encode(test)))
print("")
test = "0000,,,,##   +++"
print(test)
print(encode(test))
print(decode(encode(test)))
print("")

# took less than 15 minutes to code

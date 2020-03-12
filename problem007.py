# Problem #7 [Medium]
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
import string

# a function to encode a message using a mapping
# just change the char for a integer given by mapping
def encondeMessage(message, mapping):
    encoded = ""
    for char in message.lower():
        encoded += str(mapping[char])
    return encoded

# decode all the possibilities for the message using the mapping
def decodeMessage(message, mapping):
    decodedPossibilities = list()
    # creating a decodeMap based on the encodeMap, just changing key for value
    decodeMapping = {value: key for key, value in mapping.items()}
    print(decodeMapping)
    # saving the keys that the function will look for in the message
    textToSearch = set(decodeMapping.keys())
    print(textToSearch)
    # actual decode code
    def decoding( decodingMessage, messageToDecode):
        # if the message is empty put the decodingMessage as a possible decode
        if messageToDecode == "":
            decodedPossibilities.append(decodingMessage)
            # and stop
            return
        # it it is the last char, decode it
        if len(messageToDecode) == 1:
            decodedPossibilities.append( decodingMessage + decodeMapping[messageToDecode[0]])
            # and stop
            return
        # if the first character can be decoded without creating an undecoded message, decode it and try to decode the
        # rest of the message
        if messageToDecode[0] in textToSearch and messageToDecode[1] != "0":
            decoding( decodingMessage + decodeMapping[messageToDecode[0]], messageToDecode[1:])
        # and
        # try to decode the first and the seconde character if they are one of the keys we are looking, decode it
        # and try to decode the rest of the message
        if messageToDecode[0]+messageToDecode[1] in textToSearch:
            decoding( decodingMessage + decodeMapping[messageToDecode[0]+messageToDecode[1]], messageToDecode[2:])
    # start decoding the message
    decoding("", message)
    return decodedPossibilities

# creating the mapping
def mappingFunction():
    return {string.ascii_lowercase[index]: str(index + 1) for index in range(0,26)}

# the map used for encode/decode
mappingAlphabet = mappingFunction()
print(mappingAlphabet)

# message to encode
message = "aaa"
# encode the message
encodedMessage = encondeMessage(message, mappingAlphabet)
print(encodedMessage)

# decode all the possibilities
possibilies = decodeMessage(encodedMessage, mappingAlphabet)
print(possibilies)
for text in possibilies:
    print(text)
print(len(possibilies))

# easy and fun to do, i only had a problem when trying to decode using directly the encodeMap, but i decided to
# create a decodeMap to facilitate the transformations, my python was the only problem on this on
# took around 45 minutes, could do in less but decided to do code, decode and multiple tests, not only count it

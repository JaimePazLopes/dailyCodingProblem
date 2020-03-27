# Problem #22 [Medium]
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction,
# then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
# you should return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].


words1 = ['quick', 'brown', 'the', 'fox']
sentence1 = "thequickbrownfox"

words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
sentence2 = "bedbathandbeyond"

def originalSentence(words, sentence):
    if not words or not sentence:
        return None

    wordsInSentence = []
    sentenceSize = len(sentence)
    # while still have sentence to check
    while sentenceSize > 0:
        # for each word
        for word in words:
            size = len(word)
            # check if thi word is in the beginning of the sentence
            if word == sentence[:size]:
                # if it is, add to the answer and take this word from the sentence
                wordsInSentence.append(word)
                sentence = sentence[size:]
        else:
            # if the sentence still have the same size, no word was found and it is not possible to reconstruct
            if sentenceSize == len(sentence):
                return None
        sentenceSize = len(sentence)
    return wordsInSentence

print(originalSentence(words1, sentence1))
print(originalSentence(words2, sentence2))
print(originalSentence(words1, "quickquickfoxthebrown"))
print(originalSentence(words2, "bedbedbedbathbeyondbedandbath"))
print(originalSentence(words2, "sweetbanana"))
print(originalSentence([], "sweetbanana"))
print(originalSentence(words2, ""))
print(originalSentence(None, None))

# really easy problem, i finished in around 15 minutes. I dont think that comparing strings is the best solution,
# but in a case like this is not that serious, at least i think it is not

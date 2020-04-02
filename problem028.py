# Problem #28 [Medium]
# Write an algorithm to justify text. Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.
#
# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word. Pad extra spaces when necessary so that each line has
# exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces,
# if any, distributed starting from the left.
#
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
#
# Each word is guaranteed not to be longer than k.
#
# For example:
# given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
# you should return the following:
#
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly


# instead of passing the list of words, i decided to pass a full message and break it inside
def justify(text, k):
    # getting the words
    words = text.split()
    # variable to save the actual size of the line and see if I need to break line
    lineSize = 0
    # save all lines
    lines = []
    # save words to add to the actual line
    wordsToAdd = []
    for index in range(len(words)):
        # i get the word and add to wordstoadd, the linesize grows the size of this word
        word = words[index]
        wordsToAdd.append(word)
        lineSize += len(word)
        # if this is the last word or if I add the next word and it gets bigger than k (linesize) i create a line
        if index == len(words)-1 or lineSize + 1 + len(words[index+1]) >= k:
            # get the size of the wordstoadd
            wordCount = len(wordsToAdd)
            # get the number of extra spaces needed
            spacingSize = k - lineSize
            # if there is only one word, add it and the needed spaces
            if wordCount == 1:
                lines.append(wordsToAdd[0]+"."*spacingSize)
            else:
                # get the number of spaces between each word, the quantity of spaces need divided by the number of
                # intervals between words (wordCount-1), and +1 because it has at least the basic space
                perspace = int(spacingSize/(wordCount-1)) + 1
                # get the other spaces that cant be equally divided
                additional = spacingSize % (wordCount-1)
                line = ""
                # for each wordtoadd
                for addingWord in wordsToAdd:
                    # if it is not the first iteration, add the spacing
                    if line != "":
                        line += "."*perspace
                    # add the word
                    line += addingWord
                    # add the spacing if it is still needed
                    if additional > 0:
                        line += "."
                        additional -= 1
                # add this line to the other lines
                lines.append(line)
            # restart the line variables
            lineSize = 0
            wordsToAdd.clear()
        else:
            # if i will put another word on this line, I count the space between words
            lineSize += 1

    return lines

# just to print line by line with a len
def result(r):
    for line in r:
        print(line, len(line))
    print()

text = "the quick brown fox jumps over the lazy dog"
words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
r = justify(text, 16)
result(r)
r = justify(text, 10)
result(r)
r = justify(text, 20)
result(r)
r = justify(text, 30)
result(r)

text = '''Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of 
strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between 
each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as 
equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
 you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''
r = justify(text, 60)
result(r)

# cool problem, i got a solution in around 40 minutes, but one of my tests was wrong, and to find it took one more hour

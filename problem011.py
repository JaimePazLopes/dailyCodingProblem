# Problem #11 [Medium]
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

# i knew that this is wrong, but its all that I knew how to do, after this I went to google and discover about Tries
def autocomplete(typed, possibilities):
    matches = set()
    for word in possibilities:
        if typed == word[:len(typed)]:
            matches.add(word)
    return matches

typing = "de"
possibleWords = {"dog", "dear", "deal"}
print(autocomplete(typing, possibleWords))

# simple trie node, iscomplete is used to mark that node as the end of one word, but another word can continue from it
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.isComplete = False

# init can take all the words and insert
class TrieTree:
    def __init__(self, words=[]):
        self.root = TrieNode("*")
        if len(words) > 0:
            for word in words:
                self.insert(word)

    def insert(self, word):
        actualNode = self.root
        # foreach char[n] in the word
        for char in word:
            found = False
            # compare with each children
            for child in actualNode.children:
                # if they are a match, this node is saved and the search continue to n+1
                if char == child.char:
                    found = True
                    actualNode = child
                    break
            # if it wasnt found, it is created and positioned on its parent, after the first n all other n+1 will end here
            if not found:
                nodeToAdd = TrieNode(char)
                actualNode.children.append(nodeToAdd)
                actualNode = nodeToAdd
        # set this node as a end of word
        actualNode.isComplete = True

# get all possibilities starting on node
def partialWords(node):
    partials = []
    for child in node.children:
        # if the word is complete you add to the partials
        if child.isComplete:
            partials.append(child.char)
        # a complete word might also have children
        # for all children get its possibilities
        if len(child.children) > 0:
            childPartials = partialWords(child)
            for childPartial in childPartials:
                partials.append(child.char + childPartial)
    return partials

# look for the words that complete what was typed
def autocompleteTries(typed, words):
    tries = TrieTree(words)
    node = tries.root
    # try to find where the typed is the the tries tree, getting its node
    for char in typed:
        for child in node.children:
            if char == child.char:
                node = child
                break
        else:
            # if it was not found is because the typed has no reference in the autocomplete words
            return []
    prefix = typed
    # starting from the last node of typed, take all options of words ending
    sufix = partialWords(node)
    autocompletedWords = []
    # put together typed with all possible completions
    for partial in sufix:
        autocompletedWords.append(prefix + partial)
    return autocompletedWords

print(autocompleteTries(typing, possibleWords))

possibleWords = {"dog", "dear", "deal", "deer", "death", "banana", "delve", "dd", "de", "dew", "deals", "deal"}
print(autocompleteTries("", possibleWords))
print(autocompleteTries("x", possibleWords))
print(autocompleteTries("banana", possibleWords))  # banana is a complete word, so has no autocomplete option
print(autocompleteTries("banan", possibleWords))
print(autocompleteTries("d", possibleWords))
print(autocompleteTries("de", possibleWords))
print(autocompleteTries("dea", possibleWords))
print(autocompleteTries("deal", possibleWords))

# really cool problem, I had no idea on how to start it, so i just did a silly function that look like a sad joke
# after looking into tries. I spent around 1 hour looking into tries online and them 1 more hour doing my own
# implementation of it with the autocomplete functions

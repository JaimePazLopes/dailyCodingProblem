# Problem #13 [Hard]
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct chars.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def getLongestSubString(s,k):
    # to get all longest substring that contains at most k distinct chars
    sub = []
    testingString = ""
    testingChar = ""
    biggestSub = ""

    if k <= 0:
        return sub

    for char in s:
        # if char is already considered a distinct char add it to the testingstring
        if char in testingChar:
            testingString += char
        # if it is not, and there is space on the distinct char, add it to distinct char and testingString
        elif len(testingChar) < k:
            testingChar += char
            testingString += char
        # if there is no space on disctinc char
        elif len(testingChar) == k:
            # if the testing string has the same size as the biggest string, add it to sub
            if len(testingString) == len(biggestSub):
                biggestSub = testingString
                sub.append(biggestSub)
            # if testing string is bigger than the biggest, it becomes the biggest and reset sub
            elif len(testingString) >= len(biggestSub):
                biggestSub = testingString
                sub = []
                sub.append(biggestSub)
            # brake the testing string to remove the first distinct char, the last part of it is free from it
            testingString = testingString.split(testingString[0])[-1] + char
            # remove the first distinct char and add the new distinct char
            if len(testingChar) == 1:
                testingChar = char
            else:
                testingChar = testingChar[1:] + char
    # i am not used to for with else, so i decided to use this time, the end of s condition should be on the loop
    # to avoid code repetition
    else:
        if len(testingString) == len(biggestSub):
            biggestSub = testingString
            sub.append(biggestSub)
        elif len(testingString) >= len(biggestSub):
            biggestSub = testingString
            sub = []
            sub.append(biggestSub)
    return sub


print(getLongestSubString("a", 1))
print(getLongestSubString("a", 0))
print(getLongestSubString("abcba", 2))
print(getLongestSubString("abba", 2))
print(getLongestSubString("abcba", 1))
print(getLongestSubString("abcba", 3))
print(getLongestSubString("abcba", 5))
print(getLongestSubString("aaaabbccccbbaaaa", 1))
print(getLongestSubString("banana", 2))
print(getLongestSubString("aabacbebebe", 3))

# definitely not a hard problem, just need to go char by char saving the data necessary for all checks
# took a little more time to get all substrings, not just count the longest
# but did this one in less than 30 minutes

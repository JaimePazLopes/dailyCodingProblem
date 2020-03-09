# Problem #4 [Hard]
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

# this was the first thing that pass in my mind: if the array is sorted is easy. clearly not linear
def sortedSolution(inputArray):
    inputArray.sort()
    minInt = 1
    for number in inputArray:
        if number <= 0:
            continue
        if minInt == number:
            minInt += 1
        elif minInt > number:
            continue
        else:
            break
    return minInt
assert sortedSolution([]) == 1
assert sortedSolution([-1]) == 1
assert sortedSolution([1]) == 2
assert sortedSolution([1, 8]) == 2
assert sortedSolution([3, 4, -1, 1]) == 2
assert sortedSolution([3, 4, -1, 1, 2, 7]) == 5
assert sortedSolution([3, 4, -1, 1, 1, 1, 2, 7]) == 5
assert sortedSolution([1, 2, 0]) == 3

# dont think i can get a simpler n² solution than this, but this dont help me to see a linear solution
def sillySolution(inputArray):
    testingNumber = 0
    while True:
        testingNumber += 1
        for number in inputArray:
            if number == testingNumber:
                break
        else:
            return testingNumber

assert sillySolution([]) == 1
assert sillySolution([-1]) == 1
assert sillySolution([1]) == 2
assert sillySolution([1, 8]) == 2
assert sillySolution([3, 4, -1, 1]) == 2
assert sillySolution([3, 4, -1, 1, 2, 7]) == 5
assert sillySolution([3, 4, -1, 1, 1, 1, 2, 7]) == 5
assert sillySolution([1, 2, 0]) == 3

# the idea is to put each number on a position of the array that it is equals to its value,
# but the integer 1 will be in the first position of the array, not index = 1
# got this solution with the help of interwebs
# dont know if this is linear because of the index--
def linearSolution(inputArray):
    # if it is empty the first missing integer is 1
    if len(inputArray) == 0:
        return 1

    negativeCount = 0
    index = -1
    #loopCounter = 0 # not part of the solution, just curiosity
    # loop the list putting every number on its number = position
    while index < len(inputArray) - 1:
        index += 1
        #loopCounter += 1
        number = inputArray[index]
        # if the number is negative we dont need to swap, we are looking for positives and also there is no -index
        # other thing is that we need to know if there is only negative numbers on the array
        # if the number is bigger than the array size there is no position to swap
        # if the number is in his position we dont need to swap, remember that number 1 position 1, not index 1
        if number < 0:
            negativeCount += 1
            continue
        if number >= len(inputArray) or number == inputArray[number - 1]:
            continue

        # swap to put the number in the right position/index
        inputArray[index], inputArray[number - 1] = inputArray[number - 1], inputArray[index]
        # since we swap, we need to check this position again (it has a new value)
        # dont know if this break linear constrain, i think it does
        index -= 1

    #print(f"The array size is {len(inputArray)} and the loop was executed {loopCounter} times")

    # if there is only negative numbers, the first missing is 1
    if negativeCount >= len(inputArray):
        return 1

    # since every position has a value that is equals to the position,
    # we just need to loop to find a position that doesnt have a number equals to its position
    for index in range(len(inputArray)):
        if inputArray[index] != index + 1:
            return index + 1

    # if all positions have the numbers they are supposed to have, the array is "perfect",
    # every position has a value equals to it, so the first missing integer is +1 on its size
    return len(inputArray) + 1

assert linearSolution([3, 4, -1, 4, 4, 4, 1, 1, 1]) == 2
assert linearSolution([1, 2, 0]) == 3, "the value i got is " + str(linearSolution([1, 2, 0]))
assert linearSolution([1, 2, 5]) == 3
assert linearSolution([1]) == 2
assert linearSolution([1,2,3,4]) == 5
assert linearSolution([-1, -2]) == 1
assert linearSolution([]) == 1
assert linearSolution([-1]) == 1
assert linearSolution([1, 8]) == 2
assert linearSolution([3, 4, -1, 1]) == 2
assert linearSolution([3, 4, -1, 1, 2, 7]) == 5
assert linearSolution([3, 4, -1, 1, 1, 1, 2, 7]) == 5
assert linearSolution([9, 8, -1, 7, 13, 6, 0, 5, 4, 8, 3, 0, 2, 1]) == 10

# the first two solutions (sorted and going integer by integer) came fast, in less than 30 minutes both were thought,
# implemented and tested. the last solution was hard, i really tried to get there alone, spend more than 1 hour without
# get any solution, i just understood that to do that more linearly i would need different checks for different
# cases (i mean lots of if ... return). I also understood that i would need to run the list more than one time,
# but 2n or 3n still linear. the realization that each number could have its own position on the array came looking
# online, but it took me more than 1 hour of search and almost one more hour to implement covering every case I thought

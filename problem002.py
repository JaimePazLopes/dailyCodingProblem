# Problem #2 [Hard]
# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
# [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


# the no division on follow-up instantly give me this answer
def divisionSolution(array):
    multiplication = 1;
    for element in array:
        multiplication *= element
    resultArray = [0] * len(array)
    for index in range(0,len(array)):
        resultArray[index] = int(multiplication / array[index])
    return resultArray


array1 = [1, 2, 3, 4, 5]
resultArray1 = [120, 60, 40, 30, 24]
array2 = [3, 2, 1]
resultArray2 = [2, 3, 6]
returnArray1 = divisionSolution(array1)
returnArray2 = divisionSolution(array2)

assert returnArray1 == resultArray1, f"{returnArray1} and {resultArray1} are not the same"
assert returnArray2 == resultArray2, f"{returnArray2} and {resultArray2} are not the same"


# easy solution, but n²
def noDivisionSolution(array):
    arrayMult = [1] * len(array)
    for i in range(0,len(array)):
        for j in range(0, len(array)):
            if i != j:
                arrayMult[i] *= array[j]
    return arrayMult


returnArray1 = noDivisionSolution(array1)
returnArray2 = noDivisionSolution(array2)

assert returnArray1 == resultArray1, f"{returnArray1} and {resultArray1} are not the same"
assert returnArray2 == resultArray2, f"{returnArray2} and {resultArray2} are not the same"


# after doing the n² solution i can see a possibility of doing it as n
# the result[i] = all elements before i multiplied together * all elements after i multiplied together
# first pass gets all multiplications to the right of i
# second pass gets all multiplications to the left of i
# third pass multiply all elements before i multiplied together by all elements after i multiplied together
# got this answer by looking code online and trying to understand it
def linearSolution(array):
    # I decided that the last pass would be pure index without modifiers, so i have to do some weird index choices
    # on both previous pass

    # first pass
    # initialize the array with 1, because when multipling everything the first position do not multiply, so it is 1
    leftToRight = [1] * len(array)
    # since the first position dont multiply you can skip it here
    for index in range(1, len(leftToRight)):
        # leftToRight[index - 1] is all the previous numbers multiplied
        # array[index - 1] is the previous position that need to be multiplied on this iteration
        # leftToRight[index] is all the numbers previous to this position multiplied
        leftToRight[index] = array[index - 1] * leftToRight[index - 1]
    pass

    # second pass
    a = len(array)
    # initialize the array with 1, because when multipling everything the last position do not multiply, so it is 1
    rightToLeft = [1] * len(array)
    # since the last position dont multiply you can skip it here, len -1 would be the last elementm so len -2 to skip it
    # until -1 because the for stops on the previous count, 0. Step -1 to start on the right and go left
    for index in range(len(rightToLeft)-2, -1, -1):
        # rightToLeft[index + 1] is all the numbers that come after multiplied
        # array[index + 1] is the next position that need to be multiplied on this iteration
        # rightToLeft[index] is all the numbers that are after this position multiplied
        rightToLeft[index] = array[index + 1] * rightToLeft[index + 1]

    # third pass
    returnArray = [None] * len(array)
    for index in range(len(array)):
        # giving a position multiply all number that come after it by all number that come after it
        returnArray[index] = leftToRight[index] * rightToLeft[index]
    return returnArray

returnArray1 = linearSolution(array1)
returnArray2 = linearSolution(array2)

assert returnArray1 == resultArray1, f"{returnArray1} and {resultArray1} are not the same"
assert returnArray2 == resultArray2, f"{returnArray2} and {resultArray2} are not the same"

# took almost 3 hours, more than half of the time was spent on understanding how to get to linearSolution

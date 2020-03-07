# Problem #1 [Easy]
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

array1 = [10, 15, 3, 7]
array2 = [10, 15, 3, 7, 99, -5, 19, 4, 7, 7, -15]
k1, k2, k3, k4, k5 = 17, 0, 33, 25, 19


# easily solution, think about as soon as I read the problem
def basicSolution(array, k):
    for valueA in array:
        for valueB in array:
            if valueA + valueB == k:
                return True
    return False


assert basicSolution(array1, k1)
assert not basicSolution(array1, k2)
assert not basicSolution(array1, k3)
assert basicSolution(array1, k4)
assert not basicSolution(array1, k5)

assert basicSolution(array2, k1)
assert basicSolution(array2, k2)
assert not basicSolution(array2, k3)
assert basicSolution(array2, k4)
assert basicSolution(array2, k5)


# simple but effective improvement, got this while drawing the problem as a matrix on paper
def improvedBasicSolution(array, k):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == k:
                return True
    return False


# same solution as before, but changed to practice slicing list
def improvedBasicSolutionSliced(array, k):
    iterationCounter = 0
    for i in array:
        iterationCounter += 1
        for j in array[iterationCounter:]:
            if i + j == k:
                return True
    return False


assert improvedBasicSolution(array1, k1)
assert not improvedBasicSolution(array1, k2)
assert not improvedBasicSolution(array1, k3)
assert improvedBasicSolution(array1, k4)
assert not improvedBasicSolution(array1, k5)

assert improvedBasicSolution(array2, k1)
assert improvedBasicSolution(array2, k2)
assert not improvedBasicSolution(array2, k3)
assert improvedBasicSolution(array2, k4)
assert improvedBasicSolution(array2, k5)

assert improvedBasicSolutionSliced(array1, k1)
assert not improvedBasicSolutionSliced(array1, k2)
assert not improvedBasicSolutionSliced(array1, k3)
assert improvedBasicSolutionSliced(array1, k4)
assert not improvedBasicSolutionSliced(array1, k5)

assert improvedBasicSolutionSliced(array2, k1)
assert improvedBasicSolutionSliced(array2, k2)
assert not improvedBasicSolutionSliced(array2, k3)
assert improvedBasicSolutionSliced(array2, k4)
assert improvedBasicSolutionSliced(array2, k5)


# took me some time, but as soon as I realize that I could save information about previous visited value i got this
def linearSolution(array, k):
    possibleSolution = set()
    for value in array:
        if value in possibleSolution:
            return True
        possibleSolution.add(k - value)
    return False


assert linearSolution(array1, k1)
assert not linearSolution(array1, k2)
assert not linearSolution(array1, k3)
assert linearSolution(array1, k4)
assert not linearSolution(array1, k5)

assert linearSolution(array2, k1)
assert linearSolution(array2, k2)
assert not linearSolution(array2, k3)
assert linearSolution(array2, k4)
assert linearSolution(array2, k5)


# around 1 hour to think about the problem and get this 3 solutions

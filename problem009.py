# Problem #9 [Hard]
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
# Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5]
# should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?

# this one really got me, i could see a way of doing this, i tried but was getting a lot of problems so i give up
# and looked for a better way online. I could think in a way of doing it, but fail to code it. But i could think
# in a linear time and constant space. So i went to google

# longer and more comprehensive solution, going step by step
def getLargest(numbers):
    # giving a number in the array those variables save the maximum sum including and excluding that number,
    # included not necessary use this number in the sum, but it is taking it in consideration
    excludedSum = 0
    includedSum = numbers[0]

    for number in numbers[1:]:
        # creating a temporary sum of best sum without this number (excluded) with this number
        actualSum = excludedSum + number
        # included does not have the actual number, so it became the best sum including the previous number
        previousSum = includedSum
        # the best sum including this number is the biggest value between:
        # the previous sum and actual sum (excluded sum + actual number)
        includedSum = max(actualSum, previousSum)
        # previous sum does not have the actual number, so it becomes the excluded sum
        excludedSum = previousSum

    # return the best value including the last number in the array
    return includedSum


# using the more confusing (a, b = b, a) swap
def getLargestSwap(numbers):
    excludedSum = 0
    includedSum = numbers[0]

    for number in numbers[1:]:
        includedSum, excludedSum = max(excludedSum + number, includedSum), includedSum

    return includedSum


assert getLargest([2, 4, 6, 2, 5]) == 13
assert getLargest([5, 1, 1, 5]) == 10

assert getLargestSwap([2, 4, 6, 2, 5]) == 13
assert getLargestSwap([5, 1, 1, 5]) == 10

# this one took me around 1 hour and a half, one hour trying to do alone, then looking online and getting this solution

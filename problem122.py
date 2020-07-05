# Problem #122
#
# You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0],
# and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.
#
# For example, in this matrix
#
# 0 3 1 1
# 2 0 0 4
# 1 5 3 1
#
# The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.


def count_coins(matrix, row=0, column=0):

    if not matrix or not matrix[0]:
        return None

    # if it is the goal, return its value
    if row == len(matrix) - 1 and column == len(matrix[0]) - 1:
        return matrix[row][column]

    # go down, if possible
    way_down = matrix[row][column]
    if row < len(matrix) - 1:
        way_down += count_coins(matrix, row + 1, column)

    # go right, if possible
    way_right = matrix[row][column]
    if column < len(matrix[0]) - 1:
        way_right += count_coins(matrix, row, column + 1)

    # return the biggest count of coins
    return max(way_down, way_right)


print(count_coins(None))

print(count_coins([[]]))

print(count_coins([[0]]))

matrix = [[0, 3, 1, 1],
          [2, 0, 0, 4],
          [1, 5, 3, 1]]

print(count_coins(matrix))

matrix = [[0, 3, 1, 1],
          [2, 0, 10, 4],
          [1, 5, 3, 1]]

print(count_coins(matrix))

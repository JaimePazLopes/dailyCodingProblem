# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
#
# For example, given the following matrix:
#
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]
#
# You should print out the following:
#
# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12


def clockwise(matrix):
    # get the number of cells in the matrix
    to_visit = len(matrix) * len(matrix[0])
    # create a list to append all the elements in clockwise order
    visited = list()

    # direction will save the direction that the matrix in being visited
    direction = "right"
    # lap save the number of times the inside of the matrix has been spun
    lap = 0
    x = y = 0

    # while there is cells to visit
    while to_visit:
        # visit one cell
        to_visit -= 1
        # append it
        visited.append(matrix[y][x])
        # if the direction is right
        if direction == "right":
            # walk one step on x
            x += 1
            # if the x get to the end of the row
            if x == len(matrix[0]) - 1 - lap:
                # change the direction do down
                direction = "down"
        # elif the direction is down
        elif direction == "down":
            # walk one step on y
            y += 1
            # if the y get to the end of the column
            if y == len(matrix) - 1 - lap:
                # change direction to left
                direction = "left"
        # elif the direction is left
        elif direction == "left":
            # walk one step back on x
            x -= 1
            # if x come back to the beginning
            if x == lap:
                # change direction to up
                direction = "up"
        # elif the direction is up
        elif direction == "up":
            # walk one step back on x
            y -= 1
            # if y come back to the beginning
            if y == lap + 1:
                # finish one lap
                lap += 1
                # change direction to right
                direction = "right"

    return visited


matrix = [[1]]

assert clockwise(matrix) == [1]

matrix = [[1, 2],
          [3, 4]]

assert clockwise(matrix) == [1, 2, 4, 3]

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20]]

assert clockwise(matrix) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]

matrix = [[1,  2,  3,  4,  5],
          [6,  7,  8,  9,  10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25],
          [26, 27, 28, 29, 30]]

assert clockwise(matrix) == [1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 29, 28, 27, 26, 21, 16, 11, 6, 7, 8, 9, 14, 19, 24, 23,
                             22, 17, 12, 13, 18]

# i liked this one, at first i imagined that i would need some weird method to do it. but i think that i got a good
# idea with the direction variable controlling where to go next. finish in around 45 minutes, but most of the time was
# thinking on the problem before getting the direction idea

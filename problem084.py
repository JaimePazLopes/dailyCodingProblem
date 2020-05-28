# Problem #84
# Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water,
# so an island is a group of 1s that are neighboring and their perimeter is surrounded by water.
#
# For example, this matrix has 4 islands.
#
# 1 0 0 0 0
# 0 0 1 1 0
# 0 1 1 0 0
# 0 0 0 0 0
# 1 1 0 0 1
# 1 1 0 0 1


def explore_island(point, matrix, visited):
    # if the point is in the matrix...
    if point[0] < 0 or point[1] < 0 or point[0] >= len(matrix) or point[1] >= len(matrix[0]):
        return

    # ... if the point is an island...
    if matrix[point[0]][point[1]] == 0:
        return

    # ... and it has not been visited...
    if point in visited:
        return

    # ... add it to visit
    visited.append(point)

    # and explore the points around it
    explore_island((point[0] - 1, point[1]), matrix, visited)
    explore_island((point[0], point[1] - 1), matrix, visited)
    explore_island((point[0] + 1, point[1]), matrix, visited)
    explore_island((point[0], point[1] + 1), matrix, visited)


def count_islands(matrix):
    count = 0
    visited = list()

    # go on each cell in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if it is a island and has not been visited
            if matrix[i][j] == 1 and (i, j) not in visited:

                # count it and explore the cells around it
                count += 1
                explore_island((i, j), matrix, visited)

    return count


island_map = [[]]
assert (count_islands(island_map)) == 0

island_map = [[1]]
assert (count_islands(island_map)) == 1

island_map = [[0]]
assert (count_islands(island_map)) == 0

island_map = [[1, 0, 0, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [1, 1, 0, 0, 1],
              [1, 1, 0, 0, 1]]
assert (count_islands(island_map)) == 4

island_map = [[1, 0, 0, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0]]
assert (count_islands(island_map)) == 2

island_map = [[1, 1, 1, 1, 1],
              [0, 0, 1, 0, 1],
              [1, 1, 1, 0, 0],
              [1, 0, 1, 1, 0],
              [1, 1, 0, 1, 1],
              [1, 1, 0, 0, 1]]
assert (count_islands(island_map)) == 1

island_map = [[1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 1, 0, 1, 0],
              [1, 0, 0, 0, 1]]
assert (count_islands(island_map)) == 11

# cool problem but quite simple. finish in less than 30 minutes

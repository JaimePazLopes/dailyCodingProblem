# Problem #62 [Medium]
# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the
# top-left corner and getting to the bottom-right corner. You can only move right or down.
#
# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:
#
#     Right, then down
#     Down, then right
#
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.


def paths(N, M, position=(0, 0)):
    # if one of the dimensions are 0, there is no matrix to navigate
    if N == 0 or M == 0:
        return 0

    # if it gets on the last row or column, there is only one path from this position
    if position[0] >= N-1 or position[1] >= M-1:
        return 1
    count = 0
    # if there is more rows to go, go and get the paths
    if position[0] < N:
        count += paths(N, M, position=(position[0] + 1, position[1]))
    # if there is more columns to go, go and get the paths
    if position[0] < M:
        count += paths(N, M, position=(position[0], position[1] + 1))

    return count


assert (paths(0, 0)) == 0
assert (paths(1, 1)) == 1
assert (paths(1, 5)) == 1
assert (paths(2, 2)) == 2
assert (paths(2, 3)) == 3
assert (paths(3, 2)) == 3
assert (paths(3, 3)) == 6
assert (paths(4, 4)) == 20
assert (paths(5, 5)) == 70

# i instantly thought about this solutions, but i imagine that i could think some matrix property or some other formula
# to get the solution in a quicker way, try for around 30 minutes before giving up. took around 45 to do everything

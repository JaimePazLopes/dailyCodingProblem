# Problem #23 [Easy]
# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
# Each False boolean represents a tile you can walk on.
#
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
# the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down,
# and right. You cannot move through walls. You cannot wrap around the edges of the board.
#
# For example, given the following board:
#
# [[f, f, f, f],
# [t, t, f, t],
# [f, f, f, f],
# [f, f, f, f]]
#
# and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end
# is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

def minimumSteps(matrix, start, end, visited=None):

    if visited is None:
        visited = []

    # function to check if in a giving direction is possible to go, it has to be inside the matrix, have a False value
    # and not be visited before
    def possibleStep(matrix, start, direction, visited):
        if direction == "up" and start[0] > 0 and start not in visited:
            return not matrix[start[0]-1][start[1]]
        if direction == "down" and len(matrix) > start[0] + 1 and start not in visited:
            return not matrix[start[0]+1][start[1]]
        if direction == "left" and start[1] > 0 and start not in visited:
            return not matrix[start[0]][start[1]-1]
        if direction == "right" and len(matrix[0]) > start[1] + 1 and start not in visited:
            return not matrix[start[0]][start[1]+1]
        return False

    # this was my biggest problem, the passing is always as reference so i cant change its value direct
    # didnt had the time to look for a better solution, so i just create a copy of it
    newvisited = []
    for visit in visited:
        newvisited.append(visit)
    newvisited.append(start)

    # check if you ate in the end
    if start[0] == end[0] and start[1] == end[1]:
        return newvisited

    # check all possible move directions and add it to nextStep
    nextStep = []
    x = start[1]
    y = start[0]
    if possibleStep(matrix, start, "up", visited):
        nextStep.append((y - 1, x))
    if possibleStep(matrix, start, "down", visited):
        nextStep.append((y + 1, x))
    if possibleStep(matrix, start, "left", visited):
        nextStep.append((y, x - 1))
    if possibleStep(matrix, start, "right", visited):
        nextStep.append((y, x + 1))

    # if there is no nextStep, it is a dead end
    if len(nextStep) <= 0:
        return None

    visited = newvisited

    fastpath = None

    # for each possible move, move and try to get its best route
    for step in nextStep:
        path = minimumSteps(matrix, step, end, visited)
        if path is not None:
            if fastpath is None or len(path) < len(fastpath):
                fastpath = path

    return fastpath

f = False
t = True

matrix =[[f, f, f, f],
        [t, t, f, t],
        [f, f, f, f],
        [f, f, f, f],
        [f, f, f, f]]

start = (4, 0)
end = (0, 0)

print(minimumSteps(matrix.copy(), start, end))

matrix =[[f, f, f, f],
        [t, t, f, t],
        [f, f, f, f],
        [t, t, t, f],
        [f, f, f, f]]

print(minimumSteps(matrix.copy(), start, end))

matrix =[[f, f, f, f],
        [t, t, f, t],
        [t, t, t, t],
        [t, t, t, f],
        [f, f, f, f]]

print(minimumSteps(matrix.copy(), start, end))

# this one really got me, at the start i was not understanding why it is easy. because i thought at first in more
# complex algorithm that find the best route. but since they say that is easy, i imagine that they want a dumb one,
# no heuristics, no strategy, just check every node. I took some time to get on this, after to code was easy,
# like 15 minutes. but i took more than 1 hour to understand that i cant just pass visited, because each recursion
# will share only on list. I need to practice more my python. 2 hours to solve a simple problem. I also decided to
# change a little, and instead of the count i got the full path

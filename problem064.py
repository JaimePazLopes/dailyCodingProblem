# Problem #64 [Hard]
# A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.
#
# Given N, write a function to return the number of knight's tours on an N by N chessboard.

# all the knight movements
moves: list = [(-2, 1),
               (-1, 2),
               (1, 2),
               (2, 1),
               (-2, -1),
               (-1, -2),
               (1, -2),
               (2, -1)]


def do_knight_tour(actual_position: tuple, N: int, visited: list) -> int:
    # if all cells were visited, its is possible to do the knight tour
    if N * N == len(visited):
        return 1

    # take all the knight movements and apply to the actual position, if the new position is valid, add it to the list
    possible_moves: list = list()
    for move in moves:
        if (0 <= actual_position[0] + move[0] < N) and (0 <= actual_position[1] + move[1] < N):
            possible_moves.append((actual_position[0] + move[0], actual_position[1] + move[1]))

    count: int = 0
    # for each position on the list
    for position in possible_moves:
        # add it to the visited list if it was not visited before, and do the knight tour starting on it
        if position not in visited:
            copy_visited = visited.copy()
            copy_visited.append(position)
            # since its possible from on position to have more than one knights tour, keep them sum of them
            count += do_knight_tour(position, N, copy_visited)
    return count


# a function to to start the knight tour on all positions
def start_knight_tour(N: int) -> int:
    count: int = 0
    # for each position on the board start an knight tour
    for i in range(N):
        for j in range(N):
            starting_position: tuple = (i, j)
            visits: list = [starting_position]
            count += do_knight_tour(starting_position, N, visits)
    return count


assert (0 == start_knight_tour(0))
assert (1 == start_knight_tour(1))
assert (0 == start_knight_tour(2))
assert (0 == start_knight_tour(3))
assert (0 == start_knight_tour(4))
assert (1728 == start_knight_tour(5))

# nice problem, took almost one hour to do, but a lot of the time was to rediscover that i needed to copy the visited
# list. it is the second or third time that i fail on that

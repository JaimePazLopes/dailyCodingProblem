# Problem #67 [Medium]
# On our special chessboard, two bishops attack each other if they share the same diagonal.
# This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
#
# You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
# Write a function to count the number of pairs of bishops that attack each other.
# The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
#
# For example, given M = 5 and the list of bishops:
#
# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)
#
# The board would look like this:
#
# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
#
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.


def bishop_attack(board_size: int, bishop_positions: list) -> list:
    count = 0
    # if the board size has no cell or there is no bishop, there is no attacking bishop
    if board_size <= 0 or len(bishop_positions) <= 0:
        return count

    # removing the unnecessary cases, like 2 of the same bishop or bishops outside of the board
    clean_bishop = list()
    for bishop in bishop_positions:
        if bishop[0] < 0 or bishop[0] >= board_size or bishop[1] < 0 or bishop[1] >= board_size:
            continue
        new_bishop = (min(bishop[0], bishop[1]), max(bishop[0], bishop[1]))
        if new_bishop not in clean_bishop:
            clean_bishop.append(new_bishop)

    # compare every bishop with every bishop
    for bishop1 in clean_bishop:
        for bishop2 in clean_bishop:
            # if they are the same, ignore
            if bishop1[0] == bishop2[0] and bishop1[1] == bishop2[1]:
                continue
            # if the difference of their position is the same in both axis, they are in a diagonal
            if abs(bishop1[0] - bishop2[0]) == abs(bishop1[1] - bishop2[1]):
                count += 1

    # i took the easier solution here, i am counting every attack twice (once for each bishop) instead of doing a check
    # i went with dividing by 2
    return count//2


assert (bishop_attack(0, [(0, 0), (1, 2), (2, 2), (4, 0)])) == 0
assert (bishop_attack(5, [])) == 0
assert (bishop_attack(5, [(0, 0), (1, 2), (2, 2), (4, 0)])) == 2
assert (bishop_attack(1, [(0, 0), (1, 2), (2, 2), (4, 0)])) == 0
assert (bishop_attack(3, [(0, 0), (2, 2)])) == 1
assert (bishop_attack(5, [(0, 0), (1, 2), (2, 2), (4, 0), (-1, -1)])) == 2
assert (bishop_attack(5, [(0, 0), (1, 2), (2, 2), (4, 0), (4, 0), (4, 0), (-1, -1)])) == 2

# easy problem, the solution came in my mind immediately. took less than 30 minutes to do everything

# Problem #38 [Hard]
#
# You have an N by N board. Write a function that returns the number of possible arrangements of the board where N
# queens can be placed on the board without threatening each other, i.e. no two queens share the same
# row, column, or diagonal.


# board_columns is just the queen position on each board column
def queens_arrangements(n, board_columns=[]):
    # if it is the last column there is only on position
    if n == len(board_columns):
        return 1

    count = 0
    # try to put the queen on every index of the actual column
    for col in range(n):
        # put the queen in the position
        board_columns.append(col)
        # check if it is a valid position
        if is_valid(board_columns):
            # if it is continue to the nex column
            count += queens_arrangements(n, board_columns)
        # remove the column for next iteration
        board_columns.pop()
    return count


def is_valid(board_columns):
    # take the last queen from the last column
    current_queen_row, current_queen_col = len(board_columns) - 1, board_columns[-1]
    # Check if any queens can attack the last queen.
    for row, col in enumerate(board_columns[:-1]):
        diff = abs(current_queen_col - col)
        if diff == 0 or diff == current_queen_row - row:
            return False
    return True


assert queens_arrangements(0) == 1
assert queens_arrangements(1) == 1
assert queens_arrangements(2) == 0
assert queens_arrangements(3) == 0
assert queens_arrangements(4) == 2
assert queens_arrangements(5) == 10
assert queens_arrangements(6) == 4
assert queens_arrangements(7) == 40

# couldnt solve this, get this solution on an email that daily code problem sent me some weeks ago, change it a little
# bit to increase my comprehension

# Problem #54
# Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits.
# The objective is to fill the grid with the constraint that every row, column, and box (3 by 3 subgrid)
# must contain all of the digits from 1 to 9.
#
# Implement an efficient sudoku solver.


# test all numbers in a cell and return an array with all possibilities
def possibilities(sudoku, x, y):
    # if it is not 0, then there is already a number, so no possiblities
    if sudoku[y][x] != 0:
        return []

    possible_numbers = []
    # from 1 to 9 check if is possible to put the number, if it is append it
    for number in range(1, 10):
        if possible_at_position(sudoku, x, y, number):
            possible_numbers.append(number)
    return possible_numbers


# check a specific number in a cell
def possible_at_position(sudoku, x, y, number):
    # fix the y and change the x looking for the number, if found it, it is not possible to put it on x,y
    for test_x in range(9):
        if sudoku[y][test_x] == number:
            return False
    # fix the x and change the y looking for the number, if found it, it is not possible to put it on x,y
    for test_y in range(9):
        if sudoku[test_y][x] == number:
            return False
    squareX = (x // 3) * 3
    squareY = (y // 3) * 3
    # check if the number is in the subgrid, if it is, it is not possible to put it on x,y
    for test_x in range(3):
        for test_y in range(3):
            if sudoku[squareY + test_y][squareX + test_x] == number:
                return False
    # if nothing was found, it is possible to put the number on x,y
    return True


# just a better print to visualization
def print_sudoku(sudoku):
    for y in range(9):
        line = ""
        for x in range(9):
            line += str(sudoku[y][x]) + " "
        print(line)


def is_solved(sudoku):
    # if there is a 0 on the game, the game is not over
    if min([min(row) for row in sudoku]) == 0:
        return False
    return True


def solve(sudoku):
    # go on every cell
    for y in range(9):
        for x in range(9):
            # if there is a 0
            if sudoku[y][x] == 0:
                # look for all possible numbers and test one by one
                all_possibilities = possibilities(sudoku, x, y)
                for number in all_possibilities:
                    sudoku[y][x] = number
                    # test the number on x,y and try to solve it
                    solve(sudoku)
                    # if got a solution, return it
                    if is_solved(sudoku):
                        return sudoku
                    sudoku[y][x] = 0
                return


sudoku = [[0,0,0,0,0,0,2,0,0],
          [0,8,0,0,0,7,0,9,0],
          [6,0,2,0,0,0,5,0,0],
          [0,7,0,0,6,0,0,0,0],
          [0,0,0,9,0,1,0,0,0],
          [0,0,0,0,2,0,0,4,0],
          [0,0,5,0,0,0,6,0,3],
          [0,9,0,4,0,0,0,7,0],
          [0,0,6,0,0,0,0,0,0]]

sudoku2 = [[0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0]]

sudoku3 = [[8,0,0,0,0,0,0,0,0],
           [0,0,3,6,0,0,0,0,0],
           [0,7,0,0,9,0,2,0,0],
           [0,5,0,0,0,7,0,0,0],
           [0,0,0,0,4,5,7,0,0],
           [0,0,0,1,0,0,0,3,0],
           [0,0,1,0,0,0,0,6,8],
           [0,0,8,5,0,0,0,1,0],
           [0,9,0,0,0,0,4,0,0]]

solve(sudoku)
print_sudoku(sudoku)
print()
solve(sudoku2)
print_sudoku(sudoku2)
print()
solve(sudoku3)
print_sudoku(sudoku3)

# i lost a lot of time in a problem i couldn't even find. just deleted a big chunk of code and tried again, but lost
# easy 30 min on that. some sudoku take a long time to finish,i thought it was stuck in some endless loop, have to
# debug to see that it just take some time, more 15 minutes on this. took me around one hour and a half, BUT i have
# seen this problem before on a email the daily coding problem send me and I watched this video before:
# https://youtu.be/G_UYXzGuqvM
# even had some some notes i made about how to solve it when i saw the video the first time

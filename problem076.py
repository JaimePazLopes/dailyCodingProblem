#
# You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed
# to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is
# lexicographically later as you go down each row. It does not matter whether each row itself is ordered
# lexicographically.
#
# For example, given the following table:
#
# cba
# daf
# ghi
#
# This is not ordered because of the a in the center. We can remove the second column to make it ordered:
#
# ca
# df
# gi
#
# So your function should return 1, since we only needed to remove 1 column.
#
# As another example, given the following table:
#
# abcdef
#
# Your function should return 0, since the rows are already ordered (there's only one row).
#
# As another example, given the following table:
#
# zyx
# wvu
# tsr
#
# Your function should return 3, since we would need to remove all the columns to order it.


def min_remove(matrix):
    if not matrix:
        return 0

    count = 0
    # first row because you need to work on the column
    for row in range(len(matrix[0])):
        # get the first value on the column
        previous = matrix[0][row]
        # navigate all the column
        for column in range(1, len(matrix)):
            # if they are in order
            if previous <= matrix[column][row]:
                # save the actual
                previous = matrix[column][row]
                continue
            # if not in order count it and go to next
            count += 1
            break
    return count


matrix = [[]]

assert (min_remove(matrix)) == 0

matrix = [["a"]]

assert (min_remove(matrix)) == 0

matrix = [["c", "b", "a"],
          ["d", "a", "f"],
          ["g", "h", "i"]]

assert (min_remove(matrix)) == 1

matrix = [["a", "b", "c", "d", "e", "f"]]

assert (min_remove(matrix)) == 0

matrix = [["z", "y", "x"],
          ["w", "v", "u"],
          ["t", "s", "r"]]

assert (min_remove(matrix)) == 3

# fast and easy problem when you are used to navigate 2D matrix. took me around 15 minutes

# Problem #62 [Easy]
# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the
# matrix by going left-to-right, or up-to-down.
#
# For example, given the following matrix:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word
# 'MASS', you should return true, since it's the last row.


def has_word(matrix, word) -> bool:
    # check every cell
    for row in range(len(matrix)):
        for column in range(len(matrix[0]) - len(word) + 1):
            # if this cell is equals to the word first letter
            if matrix[row][column] == word[0]:
                # fix the row
                fixed_row = row
                # and change the column
                # this index is the word index, the word[0] is already equal, so start on the second element
                for index in range(1, len(word)):
                    # get the new column
                    advancing_column = index + column
                    # if the actual cell is not equal to the character on the word, break
                    if matrix[fixed_row][advancing_column] != word[index]:
                        break
                else:
                    # if all the word is a match, return true
                    return True
                # fix the column
                fixed_column = column
                # and change the row
                # this index is the word index, the word[0] is already equal, so start on the second element
                for index in range(1, len(word)):
                    # get the new row
                    advancing_row = index + row
                    # if the actual cell is not equal to the character on the word, break
                    if matrix[advancing_row][fixed_column] != word[index]:
                        break
                else:
                    # if all the word is a match, return true
                    return True
    return False


words = [['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S'],
         ['M', 'A', 'S', 'S']]
assert has_word(words, "FOAM")
assert has_word(words, "MASS")
assert has_word(words, "SS")
assert not has_word(words, "BANANA")
assert not has_word(words, "BANANA")
assert not has_word(words, "OO")

# cool problem, but i didnt like my solution. it is too basic and in a problem like this i think that it can be
# optimized in some way. finished in less than 30 minutes, had some problems on the advancing row and column


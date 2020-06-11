# Problem #98
#
# Given a 2D board of characters and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
# or vertically neighboring. The same letter cell may not be used more than once.
#
# For example, given the following board:
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.


def word_found(board, word, visited):
    # if there is no more letter to be found, the word was fully found
    if not word:
        return True

    # take the actual position
    last = visited[-1]

    # controller to know when the search should continue
    found = False

    # for every direction try to find the next letter on the board
    if last[0] > 0:
        point = (last[0] - 1, last[1])
        if board[point[0]][point[1]] == word[0] and point not in visited:
            new_visited = visited.copy()
            new_visited.append(point)
            found = found or word_found(board, word[1:], new_visited)
    if last[1] > 0:
        point = (last[0], last[1] - 1)
        if board[point[0]][point[1]] == word[0] and point not in visited:
            new_visited = visited.copy()
            new_visited.append(point)
            found = found or word_found(board, word[1:], new_visited)
    if last[0] < len(board) - 1:
        point = (last[0] + 1, last[1])
        if board[point[0]][point[1]] == word[0] and point not in visited:
            new_visited = visited.copy()
            new_visited.append(point)
            found = found or word_found(board, word[1:], new_visited)
    if last[1] < len(board[0]) - 1:
        point = (last[0], last[1] + 1)
        if board[point[0]][point[1]] == word[0] and point not in visited:
            new_visited = visited.copy()
            new_visited.append(point)
            found = found or word_found(board, word[1:], new_visited)
    return found


def exists(board, word):
    # look all the board for the first letter of the word
    for row in range(len(board)):
        for column in range(len(board[0])):
            # when found try to find the rest of the world
            if board[row][column] == word[0]:
                visited = list()
                visited.append((row, column))
                if word_found(board, word[1:], visited):
                    return True
    return False


board = [
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']]

print(exists(board, "ABCCED"))
print(exists(board, "SEE"))
print(exists(board, "ABCB"))

# nice problem, i finished in around 45 minutes, the hardest problem was to find a way to continue searching all
# directions each letter. solved by adding the found variable that will return false only when the word was not found
# in any of those direction

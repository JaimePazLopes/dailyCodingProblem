# Problem #56 [Medium]
# Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether
# each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors


def valid(graph, colors):
    last_vertex, last_color = len(colors) - 1, colors[-1]
    # get all neighbors
    colored_neighbors = [i
                         for i, has_edge
                         in enumerate(graph[last_vertex])
                         if has_edge and i < last_vertex]
    # for all neighbors
    for neighbor in colored_neighbors:
        # if the color is the same, you cant color with this color
        if colors[neighbor] == last_color:
            return False
    # if no color is the same, it is ok to color with this color
    return True


def colorable(graph, k, colors=[]):
    if len(colors) == len(graph):
        return True

    # for every color
    for i in range(k):
        # color it
        colors.append(i)
        # and see if this coloring is ok
        if valid(graph, colors):
            # if it is ok, try to color the next node
            if colorable(graph, k, colors):
                return True
        # if you couldnt color with this color, remove it
        colors.pop()

    return False


matrix1 = [
    [0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0]
]
assert colorable(matrix1, 4, [])
assert colorable(matrix1, 3, [])
assert not colorable(matrix1, 2, [])

# couldnt do this one, and i was feeling a little sick, so i prefer to not force myself. the good thing is that the
# solution is on the daily coding problem blog site https://www.dailycodingproblem.com/blog/graph-coloring/
# first i needed to google what undirected graph and adjacency matrix are, the first i had a good idea, because the
# name is similar to portuguese, but the last i didnt remember what it was. then i started looking for the matrix to
# see if there is a "easy" solution like counting adjacent nodes, etc. but couldnt find any.
# after i think about to try to color the graph with as little colors as possible and then compare it with k, but could
# get there. googling a solution i found the daily coding problem blog

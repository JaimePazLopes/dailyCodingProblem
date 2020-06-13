# Problem #100
#
# You are in an infinite 2D grid where you can move in any of the 8 directions:
#
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
#
# You are given a sequence of points and the order in which you need to cover the points.
# Give the minimum number of steps in which you can achieve it. You start from the first point.
#
# Example: Input: [(0, 0), (1, 1), (1, 2)] Output: 2 It takes 1 step to move from (0, 0) to (1, 1).
# It takes one more step to move from (1, 1) to (1, 2).


def get_step_distance(points):
    steps = 0

    if not points:
        return steps

    actual_point = points[0]

    # get all steps between to points
    for index in range(1, len(points)):
        next_point = points[index]

        step_x = abs(next_point[0] - actual_point[0])
        step_y = abs(next_point[1] - actual_point[1])

        # since the diagonal movement counts as 1 step, the number of steps will be the bigger value on each axis
        steps += max(step_x, step_y)

        actual_point = next_point

    return steps


assert get_step_distance([]) == 0
assert get_step_distance([(1, 1)]) == 0
assert get_step_distance([(1, 1), (1, 1), (1, 1)]) == 0
assert get_step_distance([(0, 0), (1, 1), (1, 2)]) == 2
assert get_step_distance([(0, 0), (10, 10)]) == 10
assert get_step_distance([(0, 0), (10, 0)]) == 10
assert get_step_distance([(0, 0), (10, 0), (10, 10), (0, 0)]) == 30

# the problem gets really easy when you consider a diagonal step the same length as a non diagonal. did in less than
# 30 minutes

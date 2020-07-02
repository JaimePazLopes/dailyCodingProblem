# Problem #119
#
# Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
# If there are multiple smallest sets, return any of them.
#
# For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals
# is {3, 6}.


def get_interval(intervals):

    if not intervals:
        return None

    if not intervals[0]:
        return None

    lower = intervals[0][0]
    higher = intervals[0][1]

    for interval in intervals:
        lower = max(lower, interval[0])
        higher = min(higher, interval[1])

    going = True
    try_minimum = lower
    while going:
        lower = try_minimum
        try_minimum = lower - 1
        count = 0
        for interval in intervals:
            if interval[0] <= try_minimum <= interval[1]:
                count += 1
        if count == len(intervals):
            going = False

    return [lower, higher]


print(get_interval([[0, 3], [2, 6], [3, 4], [6, 9]]))

# didnt have time enough to do it. so i stopped in the middle. will try to come back to it tomorrow

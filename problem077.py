# Problem #77 [Easy]
# Given a list of possibly overlapping intervals,
# return a new list of intervals where all overlapping intervals have been merged.
#
# The input list is not necessarily ordered in any way.
#
# For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].


def merged_intervals(intervals):
    # set to ignore equal intervals
    merged = set()

    # for each interval take it to merge
    for interval in intervals:
        merging = interval

        # try to merge with each other interval
        for to_merge in intervals:
            if interval == to_merge:
                continue

            # if there is a intersection
            # the intersection is the max starting end the min ending
            if range(max(merging[0], to_merge[0]), min(merging[1], to_merge[1])+1):
                # merge them by taking the min starting and maximum ending
                merging = (min(merging[0], to_merge[0]), max(merging[1], to_merge[1]))

        # after merging with all intervals add to the set
        merged.add(merging)

    return list(merged)


assert (merged_intervals([(1, 3), (5, 8), (4, 10), (20, 25)])) == [(20, 25), (4, 10), (1, 3)]
assert (merged_intervals([(1, 3), (5, 8), (4, 10), (20, 25), (20, 23), (-5, 2), (25, 26), (19, 20)])) == \
       [(19, 26), (4, 10), (-5, 3)]

# easy problem, spent most time thinking about how i could get the intersection in a easy way. took around 30 minutes

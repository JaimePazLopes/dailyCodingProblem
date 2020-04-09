# Problem #35 [Hard]
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
# come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
#
# Do this in linear time and in-place.
#
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


# the idea is to split the array in 3 blocks, a start block with all R, a middle block that have all G and
# a end block with all B
def order(array):

    # the start block will contain all R, the start index is the index of the next no R element
    start = 0
    # left is the index that start by the beginning of the array
    left = 0
    # right is the index that start by the end of the array and is the block with all B values,
    # the end index is the index of the next no B element
    right = len(array) - 1

    # while the left index is lower or equal to the right index, in other words,
    # while the left index has not passed the right index
    while left <= right:

        # if the actual element is R, put it on the start block, then add both index: left and start
        if array[left] == "R":
            array[left], array[start] = array[start], array[left]
            left += 1
            start += 1

        # if the actual element is G, do nothing, just add index left
        elif array[left] == "G":
            left += 1

        # if the actual element is B, put it on the end block, then reduce left index
        elif array[left] == "B":
            array[left], array[right] = array[right], array[left]
            right -= 1

    return array


assert order(['R']) == ['R']
assert order(['B', "G", 'R']) == ['R', 'G', 'B']
assert order(['R', "G", 'B']) == ['R', 'G', 'B']
assert order(['B', 'R']) == ['R', 'B']
assert order(['B', 'B', 'B', 'B']) == ['B', 'B', 'B', 'B']
assert order(['B', "G", 'B', 'R']) == ['R', 'G', 'B', 'B']
assert order(['B', 'R', "G", 'R']) == ['R', 'R', 'G', 'B']
assert order(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']
assert order(['G', 'B', 'R', 'R', 'B', 'R', 'G', 'R', 'B', 'R', 'G']) == \
       ['R', 'R', 'R', 'R', 'R', 'G', 'G', 'G', 'B', 'B', 'B']

# at first the problem scared me, but after reading it again I could think in a easy 2N solution: pass one time putting
# all R to the start then pass again passing all B to the end. It need 2 passes but it is still linear.
# With that came the possibility of doing it in one pass. i couldnt get it for some time, but after deciding to
# separate in 2 index the solution got easier. took me around 45 minutes to finish everything

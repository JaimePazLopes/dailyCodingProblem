# Problem #40 [Hard]
# Given an array of integers where every integer occurs three times except for one integer, which only occurs once,
# find and return the non-duplicated integer.
#
# For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
#
# Do this in $O(N)$ time and $O(1)$ space.


# linear time but not constant space
def non_duplicated_integer_with_dict(array):
    # a dict to count each number in array
    counting_numbers = dict()
    # for each number in the array
    for number in array:
        # if it is not in the dict, add it with its count as value
        if number not in counting_numbers.keys():
            counting_numbers[number] = 1
        # if it is on the array update its count
        else:
            counting_numbers[number] = 1 + counting_numbers[number]

    # go on each value in the dict to get the one with count equals to 1
    for key, value in counting_numbers.items():
        if value == 1:
            return key


# space is constant but time clearly is not. this method also change the element order, what could mean N space if it
# is not possible to change the order on the original array. since the problem dont clearly say that it is possible,
# i think it is not possible to change the elements position. did anyway to see a better solution.
# this method looks for all elements equal to the first one and group them at the beginning, then take the next element
# and group in the beginning after the first group and so on
def non_duplicated_constant_space(array):
    # use to swap the elements on the array using this index
    swap_index = 0
    while True:
        # where the index start in this iteration
        index_start = swap_index
        # first element in this iteration
        first = array[index_start]
        # to know if there is 3 or 1 of this element
        swaps = 0
        # for each index between the index start iteration to the end
        for index in range(index_start, len(array)):
            # if the actual element is equal the first one, change its position using the swap index
            if array[index] == first:
                # the swap
                array[index], array[swap_index] = array[swap_index], array[index]
                swap_index += 1
                swaps += 1
            # if 3 swaps happened, all numbers equal to the first one are already on the start of the array,
            # all other compares in this iteration are useless
            if swaps > 3:
                break
        # if only one swap happened means that there is only one copy of this number in the array
        if swaps == 1:
            return first


# couldnt think in a solution, got this online
def non_duplicated(array):
    answer = 0
    auxiliar = 0

    for number in array:
        auxiliar ^= answer & number
        answer ^= number
        mask = ~(answer & auxiliar)
        auxiliar &= mask
        answer &= mask

    return answer


assert non_duplicated_integer_with_dict([6, 1, 3, 3, 3, 6, 6]) == 1
assert non_duplicated_integer_with_dict([13, 19, 13, 13]) == 19

assert non_duplicated_constant_space([6, 1, 3, 3, 3, 6, 6]) == 1
assert non_duplicated_constant_space([13, 19, 13, 13]) == 19

assert non_duplicated([6, 1, 3, 3, 3, 6, 6]) == 1
assert non_duplicated([13, 19, 13, 13]) == 19

# got my 2 "solutions" in around 30 minutes, try during almost one hour to get the desired solution, but i couldnt.
# found one online, but dont know if i really understand it

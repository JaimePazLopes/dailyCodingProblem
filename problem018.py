# Problem  # 18 [Hard]
# Given an array of integers and a number k, where 1 <= k <= length of the array,
# compute the maximum values of each subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
#     10 = max(10, 5, 2)
#     7 = max(5, 2, 7)
#     8 = max(2, 7, 8)
#     8 = max(7, 8, 7)
#
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results.
# You can simply print them out as you compute them.

# this was my first and immediate thought, the max() will make it not be O(n) but is O(k)
def maximumValues(array, k):
    print(f"Checking {array} with k {k}")
    subarray = list()

    for number in array:
        if len(subarray) >= k:
            subarray.pop(0)
        subarray.append(number)
        if len(subarray) >= k:
            print(max(subarray))

# maximumValues([10, 5, 2, 7, 8, 7], 1)
# maximumValues([10, 5, 2, 7, 8, 7], 2)
# maximumValues([10, 5, 2, 7, 8, 7], 3)
# maximumValues([10, 5, 2, 7, 8, 7], 4)
# maximumValues([10, 5, 2, 7, 8, 7], 5)
# maximumValues([10, 5, 2, 7, 8, 7], 6)

# dont know if this is O(n) because there is a while loop inside, but on my calculations it will execute a small
# number of times
# for this solution i save the index not the value itself and do operations on it to always have the biggest number
# index on the position 0
def maximumValuesIndex(array, k):
    print(f"Checking {array} with k {k}")
    # list with the biggest index, this list is in order, but wont necessarily have all index, it might skip some
    indexList = list()

    # for each index on the list
    for i in range(len(array)):

        # if the i is bigger than k, i have to pay attention to remove all index that are further than the k size
        if i >= k:
            print(indexList[0])
            while len(indexList) > 0:
                # if the subarray pass the k size, remove the index
                if indexList[0] <= i - k:
                    # the index are in order, so the first position is the further element
                    indexList.pop(0)
                else:
                    break

        # this remove all index that have numbers smaller than then actual i number
        while len(indexList) > 0:
            if array[i] >= array[indexList[-1]]:
                indexList.pop()
            else:
                break

        indexList.append(i)
    else:
        # after you process the last element, print the biggest number in the subarray
        print(indexList[0])

maximumValuesIndex([10, 5, 2, 7, 8, 7], 1)
maximumValuesIndex([10, 5, 2, 7, 8, 7], 2)
maximumValuesIndex([10, 5, 2, 7, 8, 7], 3)
maximumValuesIndex([10, 5, 2, 7, 8, 7], 4)
maximumValuesIndex([10, 5, 2, 7, 8, 7], 5)
maximumValuesIndex([10, 5, 2, 7, 8, 7], 6)

maximumValuesIndex([1, 2, 3, 4, 5, 6], 3)
maximumValuesIndex([1, 2, 3, 4, 5, 6], 4)

maximumValuesIndex([6, 5, 4, 3, 2, 1], 3)
maximumValuesIndex([6, 5, 4, 3, 2, 1], 4)

maximumValuesIndex([6, -5, 1, 30, 7, 13], 3)
maximumValuesIndex([6, -5, 1, 30, 7, 13], 4)

# the problem itself is easy, doing on O(n) is what make it hard. dont know if my solution using list is the better one
# here, i imagine that it isnt, i saw other people online using deque for this problem, but i also saw that pop(0) in a
# list is O(n). so i dont know if it has any difference. The core of the algorithm was easy, took me 30 minutes,
# but some weird bug took me almost one hour to solve it.

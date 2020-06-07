# Problem #94
#
# Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least
# one node, and does not need to go through the root.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def path_sum(node: Node, actual_sum: int = 0, biggest_sum: int = 0) -> int:
    if not node:
        return biggest_sum

    # add the actual node to the sum, and get the bigger between the actual node and the sum with the working path
    actual_sum = max(node.value, actual_sum + node.value)
    # see if the actual sum is the biggest sum
    biggest_sum = max(biggest_sum, actual_sum)

    # get the sun for the left and right
    left_sum = path_sum(node.left, actual_sum, biggest_sum)
    right_sum = path_sum(node.right, actual_sum, biggest_sum)

    # get the biggest sum of all
    return max(biggest_sum, left_sum, right_sum)


assert path_sum(None) == 0

root = Node(2)
assert path_sum(root) == 2

left = Node(-1)
root.left = left
assert path_sum(root) == 2

right = Node(-3)
root.right = right
assert path_sum(root) == 2

root.right.right = Node(3)
assert path_sum(root) == 3

root.left.left = Node(10)
assert path_sum(root) == 11

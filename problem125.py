# Problem #125
#
# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
#
# For example, given the following tree and K of 20
#
#     10
#    /   \
#  5      15
#        /  \
#      11    15
#
# Return the nodes 5 and 15.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


def sum_K(root, K, nodes: set = None):
    if not root:
        return None

    if nodes is None:
        nodes = set()

    root_value = root.value

    for node in nodes:
        if root_value + node.value == K:
            return [root, node]

    nodes.add(root)

    pair = sum_K(root.left, K, nodes)
    if pair:
        return pair
    return sum_K(root.right, K, nodes)


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)

one.left = two
one.right = three
two.right = four
three.left = five
three.right = six
five.left = seven
five.right = eight

# 1
# 2 3
# 4 5 6
# 7 8

print(sum_K(one, 10))
# four.value = -20
print(sum_K(one, 3))
# five.value = -20
print(sum_K(one, 11))
# seven.value = -100
print(sum_K(one, 99))

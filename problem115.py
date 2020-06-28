# Problem #115
#
# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
# a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
# The tree s could also be considered as a subtree of itself.


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_identical(node_a, node_b):
    if node_a is None and node_b is None:
        return True
    if node_a is None or node_b is None:
        return False

    # if value is the same, the left is the same and the right is the same, the nodes are the same
    return node_a.value == node_b.value and is_identical(node_a.left, node_b.left) and \
           is_identical(node_a.right, node_b.right)


def is_subtree(s, t):
    if t is None:
        return True

    if s is None:
        return False

    # check if they are identical
    if is_identical(s, t):
        return True

    # try in the left and in the right to find an identical subtree
    return is_subtree(s.left, t) or is_subtree(s.right, t)


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
two.parent = one
three.parent = one
two.right = four
four.parent = two
three.left = five
three.right = six
five.parent = three
six.parent = three
five.left = seven
five.right = eight
seven.parent = five
eight.parent = five

print(is_subtree(one, one))
print(is_subtree(one, two))
print(is_subtree(one, six))
print(is_subtree(two, six))

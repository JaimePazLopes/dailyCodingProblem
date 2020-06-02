# Problem #89 [Medium]
# Determine whether a tree is a valid binary search tree.
#
# A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in
# the left child must be less than or equal to the root and the key in the right child must be greater than or
# equal to the root.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid(node: Node):
    if not node:
        return True

    if node.left is None and node.right is None:
        return True

    if node.left is None:
        if node.value <= node.right.value:
            return is_valid(node.right)
        return False

    if node.right is None:
        if node.left.value <= node.value:
            return is_valid(node.left)
        return False

    if node.left.value <= node.value <= node.right.value:
        return is_valid(node.left) and is_valid(node.right)

    return False


assert (is_valid(None))
assert (is_valid(Node(0)))

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)

two.left = one
two.right = three

assert (is_valid(one))
assert (is_valid(two))

three.left = four

assert (is_valid(one))
assert not (is_valid(two))
assert not(is_valid(three))


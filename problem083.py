# Problem #83
# Invert a binary tree.
#
# For example, given the following tree:
#
#     a
#    / \
#   b   c
#  / \  /
# d   e f
#
# should become:
#
#   a
#  / \
#  c  b
#  \  / \
#   f e  d


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invert(node):
    if not node:
        return

    # change left with right
    node.left, node.right = node.right, node.left

    # do the same with both sides
    invert(node.left)
    invert(node.right)


f = Node("f")
e = Node("e")
d = Node("d")
c = Node("c")
b = Node("b")
a = Node("a")

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f

invert(a)

assert a.left == c
assert a.right == b
assert a.left.right == f
assert a.right.left == e
assert a.right.right == d


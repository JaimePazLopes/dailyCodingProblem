# Problem #80
# Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
#
#     a
#    / \
#   b   c
#  /
# d


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return self.value


def deepest_node(root, depth=0):
    if not root:
        return None

    # if it is leaf return itself
    if root.left is None and root.right is None:
        return root.value, depth

    depth += 1
    left_depth = 0
    right_depth = 0
    left_node = None
    right_node = None

    # explore left
    if root.left is not None:
        left_node, left_depth = deepest_node(root.left, depth)

    # explore right
    if root.right is not None:
        right_node, right_depth = deepest_node(root.right, depth)

    # return the side with the deepest node
    if left_depth > right_depth:
        return left_node, left_depth
    return right_node, right_depth


d = Node("d")
b = Node("b")
c = Node("c")
a = Node("a")
a.left = b
a.right = c
b.left = d

print(deepest_node(a))

e = Node("e")
f = Node("f")
g = Node("g")
c.right = e
e.left = f
f.left = g

print(deepest_node(a))
print(deepest_node(d))

# it is a simple problem, i just dont like returning 2 values, maybe it is because i am not used to it, but to me looks
# bad. i was doing other things while doing this, but i think it took around 15 20 minutes.

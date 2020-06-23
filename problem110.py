# Problem #110
#
# Given a binary tree, return all paths from the root to leaves.
#
# For example, given the tree
#
#    1
#   / \
#  2   3
#     / \
#    4   5
#
# it should return [[1, 2], [1, 3, 4], [1, 3, 5]].


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def get_paths(root: Node):
    if not root:
        return None

    all_paths = list()

    # if it is leaf, return it
    if not root.left and not root.right:
        return [[root.value]]

    # explore the left
    if root.left:
        left_paths = get_paths(root.left)
        for p in left_paths:
            all_paths.append([root.value] + p)

    # explore the right
    if root.right:
        right_paths = get_paths(root.right)
        for p in right_paths:
            all_paths.append([root.value] + p)

    return all_paths


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
c.left = d
c.right = e

print(get_paths(a))

a.left = b
a.right = c
b.left = d
b.right = e
c.left = None
c.right = None

print(get_paths(a))

# the [[variable]] and append([variable]+list) always get me, i spend a lot of time trying to do the problem just
# because i cant remember those representations

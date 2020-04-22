# Problem #48 [Medium]
# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.
#
# For example, given the following preorder traversal:
#
# [a, b, d, e, c, f, g]
#
# And the following inorder traversal:
#
# [d, b, e, a, f, c, g]
#
# You should return the following tree:
#
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g


# simple node class, just add the getters and setters
class Node:
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node


# print a node in preorder, debug reasons
def preorder(root):
    tree_string = ""
    if root:
        # first value, then left, then right
        tree_string += root.value + " "
        tree_string += preorder(root.left)
        tree_string += preorder(root.right)
    return tree_string


# print a node in inorder, debug reasons
def inorder(root):
    tree_string = ""
    if root:
        # first left, then value, then right
        tree_string += inorder(root.left)
        tree_string += root.value + " "
        tree_string += inorder(root.right)
    return tree_string


# actual problem solution
def reconstruct(preorder, inorder):
    # if there is only one element, make a node and return it
    if len(preorder) == len(inorder) == 1:
        return Node(preorder[0])

    # in preorder[0] is the root of tree
    root = Node(preorder[0])

    # get the root index in inorder, everything on the left of this index is the left node,
    # everything on the right is the right node
    inorder_index = inorder.index(root.value)
    # get the len of the left nodes
    left_len = len(inorder[:inorder_index])

    # on preorder, skip the root (first element) and get the next left_len elements to reconstruct the left nodes,
    # take also all elements in inorder to the left of the root index
    root.left = reconstruct(preorder[1:left_len+1], inorder[:inorder_index])
    # on preorder, skip the root (first element) and left_len (all elements to the left) to reconstruct the right nodes,
    # take also all elements in inorder to the right of the root index
    root.right = reconstruct(preorder[1+left_len:], inorder[inorder_index+1:])

    return root


tree = reconstruct(["a", "b", "d", "e", "c", "f", "g"], ["d", "b", "e", "a", "f", "c", "g"])
print(preorder(tree))
print(inorder(tree))

tree = reconstruct(["1", "2", "4", "5", "3"], ["4", "2", "5", "1", "3"])
print(preorder(tree))
print(inorder(tree))

tree = reconstruct(["25", "15", "10", "4", "12", "22", "18", "24", "50", "35", "31", "44", "70", "66", "90"],
                   ["4", "10", "12", "15", "18", "22", "24", "25", "31", "35", "44", "50", "66", "70", "90"])
print(preorder(tree))
print(inorder(tree))

# really cool problem, at first it look possible but hard to reconstruct. After playing with the trees in a paper for
# 4 5 minutes the solution came. The reconstruct method itself was fast, testing took me much more time. finish
# everything in 30 40 minutes

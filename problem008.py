# Problem #8 [Easy]
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
# [0,[1],[0,[1,[1],[1]],[0]]]

# I decide to do everything not only count unival
# so i made a tree node class
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
# and a tree
class Tree:

    def __init__(self, nodes=None):
        self.root = None
        if nodes is not None:
            self.root = self.populate(nodes)

    def populate(self, nodes):
        if nodes is None:
            return None
        if len(nodes) == 1:
            return Node(nodes[0])
        return Node(nodes[0], self.populate(nodes[1]), self.populate(nodes[2]))

    # getting the count for univval
    # I counted as [counter, boolean], counter is the counter for unival and boolean is it the tree under this node
    # is unival or not
    def univalCount(self, root):
        # if left or right doesnt exist
        if root is None:
            return [0, True]
        # the leafs are always unival
        if root.left is None and root.right is None:
            return [1, True]
        actual = 0
        actualUnival = False
        leftUnival = self.univalCount(root.left)
        rightUnival = self.univalCount(root.right)
        # check if this node, right and left node have the same value and both need to be unival for this do be unival
        # right or left might not exist
        if root.left is None:
            if root.right.value == root.value:
                actualUnival = True
        elif root.right is None:
            if root.left.value == root.value:
                actualUnival = True
        elif root.left.value == root.right.value == root.value:
            actualUnival = True
        if actualUnival and leftUnival[1] and rightUnival[1]:
            actual = 1
        else:
            actualUnival = False
        return[leftUnival[0] + rightUnival[0] + actual, actualUnival]

    def getUnival(self):
        if self.root is None:
            return None
        return self.univalCount(self.root)[0]

    # I made this just to check if everything is being construct as it is supposed to be
    def deconstructNode(self, root):
        if root is None:
            return "None"
        value = f"[{root.value}"
        # if root.left is not None:
        value += f", {self.deconstructNode(root.left)}"
        #if root.right is not None:
        value += f", {self.deconstructNode(root.right)}"
        return value + "]"

    def deconstruct(self):
        if self.root is None:
            return ""
        return self.deconstructNode(self.root)


tree = Tree([0, [1], [0, [1, [1], [1]], [0]]])
#tree = Tree([0, None, [0]])
print(tree.deconstruct())
univalCount = tree.getUnival()
print(univalCount)

# i liked this one and decided to do it for real, so i create all the code necessary to run a count unival,
# the only problem that I had was that i stayed so focus on the example that when i started to do my own tests
# problems that are not covered in the example start to appear, if i started by solving the problem in general
# it would be easier. It took around 30 minutes to have the code running and working for the example, but when I
# started to add more complex trees the code start to broke, put around 30 ~ 45 minutes more to solve for every
# kind of tree I imagine

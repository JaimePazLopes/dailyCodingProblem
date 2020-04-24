# Problem #50 [Easy]
# Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and
# each internal node is one of '+', '−', '∗', or '/'.
#
# Given the root to such a tree, write a function to evaluate it.
#
# For example, given the following tree:
#
#     *
#    / \
#   +    +
#  / \  / \
# 3  2  4  5
#
# You should return 45, as it is (3 + 2) * (4 + 5).


# just a simple node class, probably my 10th on 50 problems hahaha
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def evaluate(root):
    # if it is a number, return it
    if root.value.isdigit():
        return int(root.value)

    # if it is a operation
    if root.value in "+-*/":
        # evaluate the left side
        l = evaluate(root.left)
        # evaluate the right side
        r = evaluate(root.right)

        # take the operation, apply and return the result
        if root.value == "+":
            return l + r
        if root.value == "-":
            return l - r
        if root.value == "/":
            return l / r
        if root.value == "*":
            return l * r


root = Node("*")

plus1 = Node("+")
n3 = Node("3")
n2 = Node("2")
plus1.left = n3
plus1.right = n2

plus2 = Node("+")
n4 = Node("4")
n5 = Node("5")
plus2.left = n4
plus2.right = n5

root.left = plus1
root.right = plus2

assert evaluate(root) == 45, evaluate(root)

# another simple problem, specially after all those node problems. took less than 10 minutes

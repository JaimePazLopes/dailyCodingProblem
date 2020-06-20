# Problem
#
# This problem was asked by Microsoft.
#
# Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
#
#   1
#  / \
# 2   3
#    / \
#   4   5


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_node(root):
    if root is None:
        return
    queue = [root]

    sequence = ""

    while queue:

        count = len(queue)

        while count > 0:
            temp = queue.pop(0)
            sequence += str(temp.value) + " "
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

            count -= 1

    print(sequence)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.left = b
a.right = c
b.left = d
b.right = e

print_node(a)

# i had some difficulties on this one, couldnt figure it out. looking online i found this
# https://www.geeksforgeeks.org/print-level-order-traversal-line-line/ changed a little the code to adapt to my way of
# thinking

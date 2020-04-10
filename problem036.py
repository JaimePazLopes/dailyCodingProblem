# Problem #36 [Medium]
# Given the root to a binary search tree, find the second largest node in the tree.

# simple node class
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.value = key


# insert on binary tree
def insert(root, node):
    # if the root is empty, became the root
    if root is None:
        root = node
    else:
        # if the new node value is bigger than the actual node value
        if root.value < node.value:
            # and there is no right node, became the right node
            if root.right is None:
                root.right = node
            # if there is right node
            else:
                # insert on this right node
                insert(root.right, node)
        # if the new node value is bigger or equals to actual node value
        else:
            # and there is no left node, became the left node
            if root.left is None:
                root.left = node
            # if there is left node
            else:
                # insert on left node
                insert(root.left, node)


# print all elements in order, only for debug reasons
def print_order(root):
    if root:
        print_order(root.left)
        print(root.val)
        print_order(root.right)


def find_second_largest(root):
    parent = root
    # if root have no node left and right, the tree has only one node, so there is no second largest value
    if parent.left is None and parent.right is None:
        return None

    # go all the way to the righ
    while root.right is not None:
        parent = root
        root = root.right

    # if this node have no right node (tested on while) and no left node, the second largest is its parent
    if root.left is None:
        return parent.value

    # take the left node
    root = root.left
    # go all the way right
    while root.right is not None:
        root = root.right

    # this is the second largest value
    return root.value


tree = Node(7)
insert(tree, Node(2))
insert(tree, Node(20))
insert(tree, Node(5))
insert(tree, Node(-10))
insert(tree, Node(2))
assert find_second_largest(tree) == 7, find_second_largest(tree)
insert(tree, Node(11))
assert find_second_largest(tree) == 11, find_second_largest(tree)
insert(tree, Node(13))
assert find_second_largest(tree) == 13, find_second_largest(tree)
insert(tree, Node(33))
assert find_second_largest(tree) == 20, find_second_largest(tree)

# it is a simple problem, took me much more time to remember how a binary tree works than to code it, did in 45 min

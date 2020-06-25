# Problem 112
#
# This problem was asked by Twitter.
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# Assume that each node in the tree also has a pointer to its parent.
#
# According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes v and w as
# the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself)."


# a simple node class with the addition of parent
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


def get_lca(node_a: Node, node_b: Node) -> Node:
    if not node_a or not node_b:
        return None

    # list with the ancestry to compare later
    node_a_ancestry = list()
    node_b_ancestry = list()

    # append all the ancestry of node a
    node = node_a
    while node is not None:
        node_a_ancestry.append(node)
        node = node.parent

    # append all the ancestry of node b
    node = node_b
    while node is not None:
        node_b_ancestry.append(node)
        node = node.parent

    # reduce the ancestry so they will have the same depth
    size = min(len(node_a_ancestry), len(node_b_ancestry))
    node_a_ancestry = node_a_ancestry[-size:]
    node_b_ancestry = node_b_ancestry[-size:]

    # try to find the common ancestor
    for index in range(size):
        if node_a_ancestry[index] == node_b_ancestry[index]:
            return node_a_ancestry[index]


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

assert get_lca(six, seven) == three
assert get_lca(five, eight) == five
assert get_lca(three, six) == three
assert get_lca(two, five) == one

# Problem #117
#
# Given a binary tree, return the level of the tree with minimum sum.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minimum_level_sum(root: Node):

    if not root:
        return None

    minimum_sum = root.value

    # this list will have the nodes to be analyzed, but the ones that will be summed in the actual iteration will be
    # on the front, in the back will be the next iteration nodes. this will be controlled by the variable count
    next_nodes = list()
    next_nodes.append(root)

    while next_nodes:
        # get the count of nodes to sum in this iteration
        count = len(next_nodes)

        actual_sum = 0

        while count > 0:
            # remove the first node and count it off
            node = next_nodes.pop(0)
            count -= 1

            # sum it
            actual_sum += node.value

            # put this node children in the list to be analyzed in the next iteration
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        minimum_sum = min(minimum_sum, actual_sum)

    return minimum_sum


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
two.right = four
three.left = five
three.right = six
five.left = seven
five.right = eight

# 1
# 2 3
# 4 5 6
# 7 8

print(minimum_level_sum(one))
four.value = -20
print(minimum_level_sum(one))
five.value = -20
print(minimum_level_sum(one))
seven.value = -100
print(minimum_level_sum(one))

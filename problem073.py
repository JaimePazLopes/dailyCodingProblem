# Problem #73 [Easy]
# Given the head of a singly linked list, reverse it in-place.


def reverse(root):
    # if there is no list, there is nothing to reverse
    if root is None:
        return

    # the initial position is root, take the next if it exists
    previous = None
    position = root
    next = None
    if position.next is not None:
        next = position.next

    # while there is a position
    while position is not None:
        # the previous become the next of the actual position
        position.next = previous
        # the actual position becomes the previous
        previous = position
        # and the next becomes the actual position
        position = next
        # if exists a next, take the next of it
        if next is not None:
            next = next.next

    # previous here will be the last element of the list
    root = previous
    return root


# simple node for a lined list
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    # starting empty list
    def __init__(self):
        self.root: Node = None

    # adding node at the end of the list
    def add(self, node: Node):
        # if root is none, node is the root
        if self.root is None:
            self.root = node
            return

        position = self.root
        # keep looking for a empty next
        while position.next is not None:
            position = position.next
        # put the node on this next
        position.next = node

    # for comparing reasons
    def __str__(self):
        text = ""

        position = self.root
        # while there is a position
        while position is not None:
            # add the value of the actual position on the text
            text += str(position.value)
            # go to next position
            position = position.next

        return text

    def reverse(self):
        # if there is no list, there is nothing to reverse
        if self.root is None:
            return

        # the initial position is root, take the next if it exists
        previous = None
        position = self.root
        next = None
        if position.next is not None:
            next = position.next

        # while there is a position
        while position is not None:
            # the previous become the next of the actual position
            position.next = previous
            # the actual position becomes the previous
            previous = position
            # and the next becomes the actual position
            position = next
            # if exists a next, take the next of it
            if next is not None:
                next = next.next

        # previous here will be the last element of the list
        self.root = previous


ll = LinkedList()
ll.reverse()
assert str(ll) == ""
ll.root = reverse(ll.root)
assert str(ll) == ""

ll = LinkedList()
ll.add(Node(1))
ll.reverse()
assert str(ll) == "1"
ll.root = reverse(ll.root)
assert str(ll) == "1"

ll = LinkedList()
ll.add(Node(1))
ll.add(Node(2))
ll.add(Node(3))
ll.add(Node(4))
ll.add(Node(5))
ll.reverse()
assert str(ll) == "54321"
ll.root = reverse(ll.root)
assert str(ll) == "12345", str(ll)

ll = LinkedList()
ll.add(Node("n"))
ll.add(Node("u"))
ll.add(Node("s"))
ll.reverse()
assert str(ll) == "sun"
ll.root = reverse(ll.root)
assert str(ll) == "nus"


# i did this method before, but never inplace. took around 45 minutes to do everything

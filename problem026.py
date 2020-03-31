# Problem #26 [Medium
#
# Given a singly linked list and an integer k, remove the kth last element from the list.
# k is guaranteed to be smaller than the length of the list.
#
# The list is very long, so making more than one pass is prohibitively expensive.
#
# Do this in constant space and in one pass.

# simple node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class List:
    # value count exists only to make it easier to create a populated list
    def __init__(self, node=None):
        self.valuecount = 0
        if node is None:
            node = Node(self.valuecount)
            self.valuecount += 1
        self.root = node

    # add a node in the end
    def add(self, node=None):
        if node is None:
            node = Node(self.valuecount)
            self.valuecount += 1

        currentNode = self.root
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node

    # remove kth last element
    def removeLastElement(self, kIndex=1):
        # previous is the previous node from the one that will be removed
        previous = self.root
        index = 0
        currentNode = self.root
        # keep going on the list until the end
        while currentNode.next is not None:
            currentNode = currentNode.next
            # wait until index pass k, after start getting next element on previous
            if index >= kIndex:
                previous = previous.next
            index += 1
        # remove the last element of the list, if it is the one to be removed
        if currentNode == previous:
            previous.next = None
        # remove the k element by skipping it
        else:
            previous.next = previous.next.next

    # print all list values
    def __str__(self):
        text = ""
        currentNode = self.root
        while currentNode.next is not None:
            text += " " + str(currentNode.value)
            currentNode = currentNode.next
        text += " " + str(currentNode.value)
        return text

l = List()
for _ in range(15):
    l.add()

l.removeLastElement()
print(l)

l = List()
for _ in range(15):
    l.add()

l.removeLastElement(3)
print(l)

l = List()
for _ in range(15):
    l.add()

l.removeLastElement(5)
print(l)

# easy problem, finish in 30 minutes. you need to go through the list keeping a pointer to the k last element,
# every time you get a next element on the list you get a next element from the pointer. when the list is finish you
# will have a pointer to the k last element

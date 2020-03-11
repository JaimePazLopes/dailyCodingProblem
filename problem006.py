# Problem #6 [Hard]
# An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
# it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
# it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

# If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
# dereference_pointer functions that converts between nodes and memory addresses.

# I decided to first do a doubly linked list to help me understand the problem and do some tests
# since the actual solution is impossible to test in python
class NodePV:

    def __init__(self, value, previous = None, next = None):
        self.value = value
        self.previous = previous
        self.next = next

    def __str__(self):
        return self.value

class DoublyLinkedList:

    def __init__(self):
        self.first = None

    def add(self, value):
        if self.first == None:
            self.first = NodePV(value)
        else:
            actualNode = self.first
            lastNode = None
            while lastNode == None:
                if actualNode.next == None:
                    lastNode = actualNode
                else:
                    actualNode = actualNode.next
            node = NodePV(value)
            actualNode.next = node
            node.previous = actualNode

    def get(self, index):
        if index < 0:
            return None
        actualNode = self.first
        countNode = 0
        while countNode != index:
            if actualNode.next == None:
                return None
            actualNode = actualNode.next
            countNode += 1
        else:
            return actualNode
        return None

    def __str__(self):
        if self.first == None:
            return "Empty List"

        returnValue = ""
        actualNode = self.first
        lastNode = None
        while lastNode == None:
            returnValue += f"{actualNode.__str__()} "
            if actualNode.next == None:
                lastNode = actualNode
            else:
                actualNode = actualNode.next
        return  returnValue

myList = DoublyLinkedList()
print(myList)
myList.add(2)
print(myList)
myList.add(5)
myList.add(8)
print(myList)
print(myList.get(0).__str__())
print(myList.get(-1).__str__())
print(myList.get(10).__str__())
print(myList.get(2).__str__())
print(myList.get(1).__str__())

class Node:

    def __init__(self, value, both = None):
        self.value = value
        self.both = both

class DoublyLinkedList:

    def __init__(self):
        self.first = None

    def add(self, value):
        if self.first == None:
            self.first = Node(value)
        else:
            previousPointer = 0
            actualNode = self.first
            lastNode = None
            while lastNode == None:
                if actualNode.both == previousPointer:
                    lastNode = actualNode
                else:
                    tempPointer = get_pointer(actualNode)
                    actualNode = dereference_pointer(actualNode.both ^ previousPointer)
                    previousPointer = tempPointer
            node = NodePV(value)
            lastNode.both = get_pointer(lastNode.both) ^ get_pointer(node)
            node.both = get_pointer(lastNode)

    def get(self, index):
        if index < 0:
            return None
        previousPointer = 0
        actualNode = self.first
        countIndex = 0
        while index != countIndex:
            if actualNode.both == previousPointer:
                return None
            tempPointer = get_pointer(actualNode)
            actualNode = dereference_pointer(previousPointer ^ actualNode.both)
            previousPointer = tempPointer
            countIndex += 1
        else:
            return actualNode

# remove red marks on code
def get_pointer(object):
    pass
def dereference_pointer(pointer):
    pass

# this problem was hard, not by the problem itself, but because I cant test my progress and the result
# it took me around 1h30m. The hardest part was doing pseudocode as final answer. I usually do the pseudocode as a start
# When I can see the next steps I go to code or I leave the details to do coding, so I can test if I am going in the
# right way. The answer itself is kinda easy if you have done a doubly linked list before, instead of having the
# previous and next value you have a XOR of them in both, so with previous and both you can do a XOR and get the next

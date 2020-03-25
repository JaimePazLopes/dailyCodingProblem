# Problem #20 [Easy]
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

# I decided to create my own node and list to control better the complexity
# simple Node class for a linked list
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def __str__(self):
        return self.value

# simple linked list with just and add method
class List:
    def __init__(self, root=None):
        if root is None:
            root = Node(0)
        self.root = root

    # add a new node in the end of the list
    def add(self, node):
        actualnode = self.root
        while True:
            if actualnode.nextNode is None:
                actualnode.nextNode = node
                break
            else:
                actualnode = actualnode.nextNode

    def __str__(self):
        toString = ""
        actualnode = self.root
        while True:
            if actualnode is None:
                break
            else:
                toString += " " + str(actualnode.__str__())
                actualnode = actualnode.nextNode
        return toString

ten = Node(10)
eight = Node(8)
eight.nextNode = ten
A = List(Node(3))
A.add(Node(7))
A.add(eight)
B = List(Node(99))
B.add(Node(1))
B.add(eight)


def startIntersection(listA, listB):
    print(listA.__str__())
    print(listB.__str__())

    # get the length of the first list
    intersection = None
    lenA = 0
    actualnode = listA.root
    while True:
        if actualnode is None:
            break
        else:
            lenA += 1
            actualnode = actualnode.nextNode

    # get the length of the second list
    lenB = 0
    actualnode = listB.root
    while True:
        if actualnode is None:
            break
        else:
            lenB += 1
            actualnode = actualnode.nextNode

    # check to see which list is bigger
    lenDif = lenA - lenB
    if lenDif < 0:
        # if B is bigger change them, I will consider that A is always bigger
        listA, listB = listB, listA
        lenDif = abs(lenDif)


    actualnodeA = listA.root
    actualnodeB = listB.root
    while True:
        if actualnodeA is None or actualnodeB is None:
            return "No intersection found"
        # keep getting the next Node on A until A and B have the same size
        if lenDif > 0:
            actualnodeA = actualnodeA.nextNode
            lenDif -= 1
            continue
        # if both have the same size check if the actualNode on both is the same Node
        if actualnodeA == actualnodeB:
            # if they are, this is the intersection
            intersection = actualnodeA
            break
        # if they arent get the next Node
        actualnodeA = actualnodeA.nextNode
        actualnodeB = actualnodeB.nextNode

    return intersection

print(startIntersection(A, B).__str__())

C = List(Node(77))
C.add(Node(8))
C.add(Node(88))
C.add(Node(-30))
C.add(eight)

print(startIntersection(A, C).__str__())
print(startIntersection(C, B).__str__())

D = List(Node(1))
D.add(Node(2))
D.add(Node(3))

print(startIntersection(C, D).__str__())

# another simple problem that the restriction made hard, I dont know if my code is O(M+N). I know it could be even
# better if the list save the size, as most implementation do. if i did the worst case would be the size of the
# smaller list. I have to study complexity in more details.
# This took less than one hour, the biggest time spent was trying to think how to go to O(M+N)

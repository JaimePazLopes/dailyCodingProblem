# Problem #78 [Medium]
# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.


# just a simple linked node
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
            return

        actual = self.head

        while actual.next:
            actual = actual.next
        actual.next = node

    # to print the result
    def __str__(self):
        text = ""

        node = self.head

        while node:
            text += str(node.value) + " "
            node = node.next

        return text


def merge_two_lists(node1, node2):
    node = None

    # if one of the lists is over, just take everything from the other one
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    # take the lowest value and its next is the merge of its old next and the other
    if node1.value <= node2.value:
        node = node1
        node.next = merge_two_lists(node1.next, node2)
    else:
        node = node2
        node.next = merge_two_lists(node1, node2.next)

    return node


def merge_lists(lists):
    merged = LinkedList()

    if not lists:
        return merged

    # take the first list
    node = lists[0].head
    # merge it with all the others
    for index in range(1, len(lists)):
        node = merge_two_lists(node, lists[index].head)

    merged.head = node
    return merged


# just to create the necessary lists easier
def create_list(numbers):
    l = LinkedList()

    for number in numbers:
        l.append(Node(number))

    return l


l1 = [3, 4, 7, 9, 14]
l2 = [-1, 2, 4, 5, 6, 19]
l3 = [8]

print(merge_lists([]))
print(merge_lists([create_list(l1)]))
print(merge_lists([create_list(l3)]))
print(merge_lists([create_list(l1), create_list(l2)]))
print(merge_lists([create_list(l1), create_list(l3)]))
print(merge_lists([create_list(l2), create_list(l3)]))
print(merge_lists([create_list(l1), create_list(l2), create_list(l3)]))
print(merge_lists([create_list(l3), create_list(l1), create_list(l2)]))
print(merge_lists([create_list(l2), create_list(l1), create_list(l2)]))

# i tried for a good hour do a function that that multiple lists and merge all at the same time, but couldnt do it.
# so i took a step back and merge them 2 by 2, much simpler solution, but definitely not the best. did everything in one
# hour and 30 minutes

# Problem #127
#
# Let's represent an integer in a linked list format by having each node represent a digit in the number.
# The nodes make up the number in reversed order.
#
# For example, the following linked list:
#
# 1 -> 2 -> 3 -> 4 -> 5 is the number 54321.
#
# Given two linked lists in this format, return their sum in the same linked list format.
#
# For example, given
#
# 9 -> 9 5 -> 2 return 124 (99 + 25) as:
#
# 4 -> 2 -> 1


# simple linked node
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class List:
    def __init__(self, number=None):
        self.root = None

        node = None

        # if a number was given the list is populated
        if number:
            for digit in str(number):
                if not node:
                    node = Node(int(digit))
                    continue
                n = Node(digit, node)
                node = n

        self.root = node

    # for print purposes
    def __repr__(self):
        message = ""
        root = self.root
        while root:
            message += str(root.value)
            root = root.next
        return message[::-1]


def sum_lists(list_a: List, list_b: List):
    if not list_a and list_b:
        return list_b
    if list_a and not list_b:
        return list_a
    if not list_a and not list_b:
        return None

    # cursors will control the advancing steps in the list
    cursor_a = list_a.root
    cursor_b = list_b.root
    # carry is the "goes one" that happens when + numbers like 5 + 5. dont know exactly the names for that in english
    carry = 0

    node = None
    answer = List()

    # while there is a next node in any of the lists
    while cursor_a or cursor_b:
        value_a = 0

        # if there is a node in a get its value and go to next node
        if cursor_a:
            value_a = cursor_a.value
            cursor_a = cursor_a.next

        # if there is a node in b get its value and go to next node
        value_b = 0
        if cursor_b:
            value_b = cursor_b.value
            cursor_b = cursor_b.next

        # add them together and with carry
        value = int(value_a) + int(value_b) + int(carry)

        # if the sum is bigger than 10, there is a carry
        if value >= 10:
            carry = 1
            digit = value % 10
        else:
            carry = 0
            digit = value

        # if no node was made, make one and add as root
        if not node:
            node = Node(int(digit))
            answer.root = node
            continue
        # create and add the next node in the list
        n = Node(digit)
        node.next = n
        node = n

    # if after all the sum,
    if carry == 1:
        n = Node(1)
        node.next = n

    return answer


first = List(54321)
print(first)

second = List(99)
print(second)

third = List(25)
print(third)

print(sum_lists(second, third))

print(sum_lists(List(333), List(999)))
print(sum_lists(List(1), List(999)))
print(sum_lists(List(1), None))
print(sum_lists(None, List(999)))
print(sum_lists(None, None))

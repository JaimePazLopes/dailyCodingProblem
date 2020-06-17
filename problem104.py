# Problem #104
#
# Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
#
# For example, 1 -> 4 -> 3 -> 4 -> 1 returns true while 1 -> 4 returns false.


class SingleNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


def is_palindrome_double(data):
    data_end = data

    while data_end.next is not None:
        data_end = data_end.next

    while data is not None:
        if data.value != data_end.value:
            return False
        data = data.next
        data_end = data_end.previous

    return True


def is_palindrome_single(data):
    values = list()

    while data is not None:
        values.append(data.value)
        data = data.next

    return values == values[::-1]


def is_palindrome(data):
    if type(data) == DoubleNode:
        return is_palindrome_double(data)
    return is_palindrome_single(data)


double_list = DoubleNode(2)
node_a = DoubleNode(15)
double_list.next = node_a
node_a.previous = double_list
assert not (is_palindrome(double_list))

node_b = DoubleNode(2)
node_a.next = node_b
node_b.previous = node_a
assert (is_palindrome(double_list))


double_list = DoubleNode(1)
node_a = DoubleNode(4)
double_list.next = node_a
node_a.previous = double_list
assert not (is_palindrome(double_list))

node_b = DoubleNode(3)
node_a.next = node_b
node_b.previous = node_a
node_c = DoubleNode(4)
node_b.next = node_c
node_c.previous = node_b
node_d = DoubleNode(1)
node_c.next = node_d
node_d.previous = node_c
assert (is_palindrome(double_list))


single_list = SingleNode(2)
single_list.next = SingleNode(15)
assert not (is_palindrome(single_list))

single_list.next.next = SingleNode(2)
assert (is_palindrome(single_list))


single_list = SingleNode(1)
node_a = SingleNode(4)
single_list.next = node_a
assert not (is_palindrome(single_list))

node_b = SingleNode(3)
node_a.next = node_b
node_c = SingleNode(4)
node_b.next = node_c
node_d = SingleNode(1)
node_c.next = node_d
assert (is_palindrome(single_list))

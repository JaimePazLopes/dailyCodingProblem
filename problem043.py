# Problem #43 [Easy]
# Implement a stack that has the following methods:
#
#     push(val), which pushes an element onto the stack
#     pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack,
#     then it should throw an error or return null.
#     max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
#     then it should throw an error or return null.
#
# Each method should run in constant time.


class Stack:
    def __init__(self):
        # list with all elements in the order they are place in
        self.elements = []
        # in each position of this list there is the max value considering all values before it
        self.max_elements = []

    def push(self, val):
        # elements dont need any kind of special control, so just append to elements
        self.elements.append(val)
        # if max elements is empty, just append to it
        if not self.max_elements:
            self.max_elements.append(val)
        # but if there is a max on it, append the max between the val to be add and the last value on this list
        else:
            self.max_elements.append(max(val, self.max_elements[-1]))

    def pop(self):
        if not self.elements:
            return None
        # just pop from both lists
        self.max_elements.pop()
        return self.elements.pop()

    def max(self):
        # if there is something on the list, return the last value
        if not self.max_elements:
            return None
        return self.max_elements[-1]


stack = Stack()
assert stack.pop() is None
assert stack.max() is None
stack.push(2)
stack.push(5)
stack.push(-1)
assert stack.max() == 5
stack.push(55)
assert stack.max() == 55
assert stack.pop() == 55
assert stack.max() == 5
assert stack.pop() == -1
assert stack.pop() == 5
assert stack.max() == 2
assert stack.pop() == 2
assert stack.pop() is None
assert stack.max() is None
stack.push(-1)
assert stack.max() == -1
assert stack.pop() == -1
assert stack.pop() is None

# cool problem, but with easy solution. Took 30 minutes to do it, and I even start ignoring "constant time" and
# began doing a more common stack implementation

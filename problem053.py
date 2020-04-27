# Problem #53 [Medium]
# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the
# following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


class Queue:

    # create both stacks, one will actually save all the elements, the other is just to support the removing method
    def __init__(self):
        self._stack = list()
        self._supporting_stack = list()

    # to add tp the queue simple add it to the stack list
    def enqueue(self, element):
        self._stack.append(element)

    # to remove use the supporting stack to save all elements except the one to be removed, the last element on stack
    # after removing it, add all elements again to the stack
    def dequeue(self):
        stack_size = len(self._stack)
        if stack_size <= 0:
            return None
        # transfer all elements except the last
        for _ in range(stack_size - 1):
            self._supporting_stack.append(self._stack.pop())
        # remove the last element
        removing_element = self._stack.pop()
        # transfer all elements back
        for _ in range(stack_size - 1):
            self._stack.append(self._supporting_stack.pop())
        return removing_element


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
assert queue.dequeue() == 1
assert queue.dequeue() == 2
assert queue.dequeue() == 3
queue.enqueue(5)
queue.enqueue(6)
assert queue.dequeue() == 4
assert queue.dequeue() == 5
assert queue.dequeue() == 6
assert queue.dequeue() is None

# nice problem, at first i was a little lost, but in some minutes i understood that i just need to transfer from on
# stack to the other, and then transfer back. Took around 20 25 minutes to finish everything

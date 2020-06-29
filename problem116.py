# Problem #116
#
# Generate a finite, but an arbitrarily large binary tree quickly in O(1).
#
# That is, generate() should return a tree whose size is unbounded but finite.

import random


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self._left = left
        self._right = right

        self._is_left_evaluated = False
        self._is_right_evaluated = False

    @property
    def left(self):
        if not self._is_left_evaluated:
            rnd = random.random()
            if rnd < 0.5:
                self._left = Node(rnd)

        self._is_left_evaluated = True
        return self._left

    @property
    def right(self):
        if not self._is_right_evaluated:
            rnd = random.random()
            if rnd < 0.5:
                self._right = Node(rnd)

        self._is_right_evaluated = True
        return self._right


def generate():
    return Node(0)


node = generate()

# didnt liked this one, sounds like a trick question and not a proper challenge. after some time thinking about it i
# decided to go online and found this answer on the official daily coding challenge site.

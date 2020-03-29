# Problem #24 [Medium]
# Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants
# or ancestors are not locked.
#
# Design a binary tree node class with the following methods:
#
#     is_locked, which returns whether the node is locked
#     lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise,
#     it should lock it and return true.
#     unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise,
#     it should unlock it and return true.
#
# You may augment the node to add parent pointers or any other property you would like.
# You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes.
# Each method should run in O(h), where h is the height of the tree.

class Node:
    # didnt like this constructor, specially because i am doing everything here, but i didnt have the time to do
    # it in a better way
    def __init__(self, value, left=None, right=None, locked=False, parent=None):
        # value exist just to guide me on checking the tree creation
        self.value = value
        self.left = left
        # if there is a left, this node is the left parent
        if self.left is not None:
            self.left.parent = self
        self.right = right
        # if there is a right, this node is the right parent
        if self.right is not None:
            self.right.parent = self
        self.locked = locked
        self.parent = parent

    # check if it is lock is a simple return in the locked
    def isLocked(self):
        return self.locked

    def lock(self):
        # to lock no parent can be locked and no child can be locked
        if not self.isParentLocked() and not self.isChildLocked():
            self.locked = True
            return True
        return False

    def unlock(self):
        # to unlock no parent can be locked and no child can be locked
        if not self.isParentLocked() and not self.isChildLocked():
            self.locked = False
            return True
        return False

    # check if any of it parents parents is locked
    def isParentLocked(self):
        # if there is no parent, there is no parent locked
        if self.parent is None:
            return False
        # if a parent is locked
        if self.parent.locked:
            return True
        # check if its parent parent is locked
        return self.parent.isParentLocked()

    # hate all this ifs, but didnt had time to do it better, if any of its child is locked return true
    # keep searching in its childs childs until get to a leaf or found a locked child
    def isChildLocked(self):
        if self.right is None and self.left is None:
            return False
        if self.right is not None and self.right.locked:
            return True
        if self.left is not None and self.left.locked:
            return True
        if self.right is not None and self.left is None:
            return self.right.isChildLocked()
        if self.right is None and self.left is not None:
            return self.left.isChildLocked()
        if self.right is not None and self.left is not None:
            return self.right.isChildLocked() or self.left.isChildLocked()

node1 = Node(1)
node2 = Node(2, right=node1)
node3 = Node(3)
node4 = Node(4, left=node2, right= node3)
node5 = Node(5, locked=True)
node6 = Node(6)
node7 = Node(7, left=node5)
node8 = Node(8, left=node6, right=node7)
root = Node(0, left=node8, right=node4)

print(node3.isLocked())
print(node5.isLocked())
print(node7.lock())
print(node1.lock())
print(node5.unlock())
print(node7.lock())
print(node5.isLocked())
print(node7.isLocked())
print(node5.lock())
print(root.lock())
print(node1.lock())

# simple problem, sadly i didnt had the time to do it in a cleaner way. Maybe i can came back to it later

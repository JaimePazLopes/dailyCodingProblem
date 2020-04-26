# Problem #52 [Hard]
# Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n,
# and contain the following methods:
#
# set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
# then it should also remove the least recently used item. get(key): gets the value at key.
# If no such key exists, return null. Each operation should run in O(1) time.


# double linked node
class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


class LRU:
    def __init__(self, n):
        # set max size
        self.n = n
        # the actual cached information
        self.cached_data = dict()
        # both head and tail are not elements on the list, they are just pointers to the actual list with the
        # order of elements use
        self.head = DoubleNode(None, None)
        self.tail = DoubleNode(None, None)
        # at the beginning they point to each other
        self.head.next = self.tail
        self.tail.previous = self.head

    # removing is taking the pointers point to the actual note and make the point to the previous or next of this node
    def _remove(self, node):
        nprevious = node.previous
        nnext = node.next
        nprevious.next = nnext
        nnext.previous = nprevious

    # since the tail is not a element itself just a pointer to the actual tail, so adding an element is putting it on
    # the second last position. Take the tail and put a node before it
    def _add(self, node):
        tprevious = self.tail.previous
        tprevious.next = node
        self.tail.previous = node
        node.previous = tprevious
        node.next = self.tail

    # update a node is remove it and add it again, to update its position on the list
    def _update(self, node):
        self._remove(node)
        self._add(node)

    def get(self, key):
        # if the key exists
        if key in self.cached_data:
            # take it
            node = self.cached_data[key]
            # update the node position on the order of uses list
            self._update(node)
            # return it
            return node.value
        # if dont exist, return None
        return None

    def set(self, key, value):
        # create the node with the parameters
        node = DoubleNode(key, value)
        # if the key exists
        if key in self.cached_data:
            # remove it, to add the new one in the sequence, updating it value and position on the use array
            self._remove(self.cached_data[key])
        # add the node on the list of uses
        self._add(node)
        # cache the node
        self.cached_data[key] = node
        # if the cache has more elements that the max
        if len(self.cached_data) > self.n:
            # the head point to the last use element, so take it to remove
            node = self.head.next
            # remove from the use order list
            self._remove(node)
            # remove from cache
            del self.cached_data[node.key]


lru = LRU(3)
assert lru.get("a") is None
lru.set("a", 333)
assert lru.get("a") == 333
lru.set("bb", 1)
lru.set("c", "banana")
lru.set("z", "zeta")
assert lru.get("a") is None
assert lru.get("c") == "banana"
assert lru.get("bb") == 1
lru.set("bb", 2)
assert lru.get("bb") == 2
lru.set("a", 333)
assert lru.get("bb") == 2
assert lru.get("c") == "banana"
assert lru.get("z") is None

# time complexity always get me, so i looked online and found this https://wiki.python.org/moin/TimeComplexity
# get, set[] and delete on dict is on average O(1), with a weird worst case that i actually didnt understood,
# but the more i google the more it looks rare and improbable, so i will go with it. i tried to do the order of use list
# with order structures, but couldnt think on a way to solve it. Looking online i found the double linked list where you
# keep the head and tail just as pointers to the actual elements. did it in around one hour and a half,
# most time looking stuff online

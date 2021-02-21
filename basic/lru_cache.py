import collections
# cache eviction based on the least recently used item
# get least recently used item in O(1)
# add/update any item in O(1)
# space O(n) hash map and linked list


# with Double Linked List
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class LRUCache(object):
    def __init__(self, capacity):
        self.head = Node(-1) # less frequent to the left
        self.tail = self.head # most frequent
        self.d = {} # key to Node
        self.capacity = capacity
        self.len = 0

    def _hit(self, n):
        if n.right:
            # remove node from its place
            n.left.right = n.right
            n.right.left = n.left
            n.right = None
            n.left = None
            # put it at the end
            self._update(n)

    def _update(self, n):
        # insert node to the end
        self.tail.right = n
        n.left = self.tail
        self.tail = n

    def get(self, key):
        if key not in self.d:
            return -1
        n = self.d[key]
        self._hit(n)
        return n.val

    def put(self, key, value):
        if key in self.d:
            n = self.d[key]
            n.val = value
            self._hit(n)
            return

        n = Node(value)
        self.d[key] = n
        self._update(n)

        self.len += 1
        if self.len > self.capacity:
            del self.d[self.head.right.key]
            self.head.right = self.head.right.right
            self.head.right.left = self.head
            self.len -= 1


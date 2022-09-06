import collections
# cache eviction based on the least frequently used item
# at put (new item) invalidate the least frequently used item (in case of tie evict the least recently used)

class LFUCache:

    def __init__(self, capacity):
        # freq to dict { key to (value, freq) }
        self.freq = defaultdict(collections.OrderedDict)
        self.d = dict() # key to Node
        self.capacity = capacity
        self.least_freq = 1

    def _update(self, key, val):
        _, f = self.d[key]
        self.freq[f].pop(key)

        if len(self.freq[self.least_freq]) == 0:
            self.least_freq += 1

        self.freq[f+1][key] = (val, f+1)
        self.d[key] = (val, f+1)

    def get(self, key):
        if key not in self.d:
            return -1
        val = self.d[key][0]
        self._update(key, val)
        return val

    def put(self, key, val):
        if key in self.d:
            self._update(key, val)
            return
        self.d[key] = (val, 1)
        self.freq[1][key] = (val, 1)
        if self.capacity == 0:
            removed = self.freq[self.least_freq].popitem(last=False)
            self.d.pop(removed[0])
        else:
            self.capacity -= 1
        self.least_freq = 1






# my AAARGH working solution with list of frequency lists


class Node:
    def __init__(self, key, val):
        # also keep the key and frequency
        self.key = key
        self.freq = 1
        self.val = val
        self.left = None
        self.right = None

class FreqList:
    def __init__(self):
        self.head = Node(-1, -1) # oldest added
        self.tail = self.head # most recently added

    def remove(self, n):
        # removes the given node from the chain
        # print('remove', n.key, n.freq)
        if self.tail.key == n.key: # edgecase when node is the only one
            self.tail = n.left
            self.tail.right = None
            return
        n.left.right = n.right
        n.right.left = n.left
        n.right = None
        n.left = None

    def update(self, n):
        # adds given node to the end
        # print('add', n.key, n.freq)
        self.tail.right = n
        n.left = self.tail
        self.tail = n


class LFUCache:

    def __init__(self, capacity: int):
        self.freq = {}  # freq to List
        self.freq[1] = FreqList()
        self.d = {} # key to Node
        self.capacity = capacity
        self.len = 0

    def remove_least_freq(self):
        # fkeys = sorted(list(self.freq.keys()))
        for f in range(10000):
            if f in self.freq:
                l = self.freq[f]
                n = l.head.right
                if n != None:
                    key_to_delete = n.key
                    l.remove(n)
                    return key_to_delete
        return None

    def _hit(self, n):
        f = n.freq
        l = self.freq[f]
        key_to_delete = l.remove(n)
        n.freq += 1
        self._update(n)

    def _update(self, n):
        f = n.freq
        if f in self.freq:
            l = self.freq[f]
        else:
            l = FreqList()
            self.freq[f] = l
        l._update(n)

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.d[key]
            self._hit(n)
            # self.print()
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.d:
            n = self.d[key]
            n.val = value
            self._hit(n)
            return
        n = Node(key, value)
        self.d[key] = n
        self.len += 1
        if self.len > self.capacity:
            key_to_delete = self.remove_least_freq()
            del self.d[key_to_delete]
            self.len -= 1
        self._update(n)
        # self.print()

    # def print(self):
    #     for x in self.d.values():
    #         print(x.key, x.val, x.freq, end=", ")
    #     print("")
    #     print(self.freq.keys())
    #     print("")


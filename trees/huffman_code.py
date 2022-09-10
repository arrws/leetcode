import heapq

class Node:
    def __init__(self, val, freq, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.freq = freq

def huffman_code(data, freq):
    # heap of (frequency, Node)
    q = [(f, Node(val, f)) for val, f in zip(data, freq)]
    heapq.heapify(q)
    while len(q) > 1:
        # take the least frequent 2 elements
        fx, x = heapq.heappop(q)
        fy, y = heapq.heappop(q)
        # unite them in new node
        z = Node('#', fx + fy, x, y)
        heapq.heappush(q, (z.freq, z))
    return q[0]

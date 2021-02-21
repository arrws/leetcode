class MinHeap:
    def __init__(self):
        self.h = [0]

    def _swap(self, x, y):
         u = self.h[x]
         self.h[x] = self.h[y]
         self.h[y] = u


    def _go_down(self, x):
        left = 2*x
        right = 2*x+1

        if right < len(self.h):
            if self.h[x] > self.h[left] and self.h[left] <= self.h[right]:
                self._swap(x, left)
                self._go_down(left)
            if self.h[x] > self.h[right] and self.h[right] <= self.h[left]:
                self._swap(x, right)
                self._go_down(right)

        # no right element
        if left < len(self.h) and self.h[x] > self.h[left]:
                self._swap(x, left)
                self._go_down(left)


    def _go_up(self, x):
        parent = int(x/2)
        if x>1 and self.h[x] < self.h[parent]:
            # print(self.h)
            self._swap(x, parent)
            self._go_up(parent)


    def heapify(self, v):
        self.h = [0]
        for x in v:
            self.push(x)

    def push(self, x):
        self.h.append(x)
        self._go_up(len(self.h)-1)

    def pop(self):
        x = self.h[1]
        self._swap(1, len(self.h)-1)
        self.h.pop(-1)
        self._go_down(1)
        return x

    def print_tree(self):
        p = 1
        j = 0
        while p < len(self.h):
            for i in range(p, p*2):
                if i < len(self.h):
                    print(self.h[i], end=" ")
                    # print(i, end=" ")
            j += 1
            p = int(pow(2,j))
            print("")
        print("")


def Node():
    def __init__(self, v=0):
        self.value = v
        self.right = None
        self.left = None

def merge_heaps(h1, h2):
    # basecase
    if not h1 or not h2:
        return h1 if h1 else h2

    # set on h1 the smallers head tree
    if h2.value < h1.value:
        h1, h2 = h2, h1

    # randomly choose child to merge to
    if random.randint(1) == 0:
        h1.left = merge_heaps(h1.left, h2)
    else:
        h1.right = merge_heaps(h1.right, h2)
    return h1


v = [5,12,23,7,15,29,30,11,2,8,36,16,10]
print("heapify",v)

h = MinHeap()
h.heapify(v)
h.print_tree()

h.pop()
h.print_tree()

print("add",9,20,"pop")
h.push(9)
h.push(20)
h.pop()
h.print_tree()

print("add",19,4,"pop")
h.push(19)
h.push(4)
h.pop()

h.print_tree()


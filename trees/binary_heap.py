class MinHeap:
    def __init__(self):
        self.arr = [0]

    def _swap(self, x, y):
         u = self.arr[x]
         self.arr[x] = self.arr[y]
         self.arr[y] = u


    def _go_down(self, x):
        left = 2*x
        right = 2*x+1

        if right < len(self.arr):
            # change with the smaller one
            i = left if self.arr[left] <= self.arr[right] else right
            if self.arr[x] > self.arr[i]:
                self._swap(x, i)
                self._go_down(i)

        # no right element
        if left < len(self.arr) and self.arr[x] > self.arr[left]:
                self._swap(x, left)
                self._go_down(left)


    def _go_up(self, x):
        parent = int(x/2)
        if x>1 and self.arr[x] < self.arr[parent]:
            # print(self.arr)
            self._swap(x, parent)
            self._go_up(parent)


    def heapify(self, v):
        self.arr = [0]
        for x in v:
            self.push(x)

    def push(self, x):
        self.arr.append(x)
        self._go_up(len(self.arr)-1)

    def pop(self):
        x = self.arr[1]
        self._swap(1, len(self.arr)-1)
        self.arr.pop(-1)
        self._go_down(1)
        return x

    def print_tree(self):
        p = 1
        j = 0
        while p < len(self.arr):
            for i in range(p, p*2):
                if i < len(self.arr):
                    print(self.arr[i], end=" ")
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


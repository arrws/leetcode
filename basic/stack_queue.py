# minimum in O(1)

class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        m = min(self.s[-1][1], x) if len(self.s) > 0 else x
        self.s.append((x, m))

    def _put(self, x):
        self.s.append(x)

    def pop(self):
        x, _ = self.s.pop(-1)
        return x

    def get_min(self):
        return self.s[-1][1] if len(self.s) > 0 else None

    def check(self):
        return len(self.s) > 0

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        if not self.s2.check():
            while self.s1.check():
                x = self.s1.pop()
                self.s2.push(x)
        return self.s2.pop()

    def get_min(self):
        mn1 = self.s1.get_min();
        mn2 = self.s2.get_min();
        if not mn1 and not mn2:
            return None
        elif not mn1:
            return mn2
        elif not mn2:
            return mn1
        else:
            return min(mn1, mn2)

q = Queue()
q.push(10)
q.push(5)
q.push(8)
q.push(2)
q.pop()
q.pop()
q.pop()
q.push(5)
q.push(6)
q.push(4)
q.pop()


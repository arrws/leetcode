class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.h = 1

class AVL_Tree():
    def insert(self, x, key):
        if not x:
            return Node(key)
        elif key < x.val:
            x.left = self.insert(x.left, key)
        else:
            x.right = self.insert(x.right, key)

        # update ancestor node height
        x.h = 1 + max(self.get_height(x.left), self.get_height(x.right))

        balance = self.get_balance(x)

        # unbalanced node
        # Left Left
        if balance > 1 and key < x.left.val:
            return self.rotate_right(x)
        # Right Right
        if balance < -1 and key > x.right.val:
            return self.rotate_left(x)
        # Left Right
        if balance > 1 and key > x.left.val:
            x.left = self.rotate_left(x.left)
            return self.rotate_right(x)
        # Right Left
        if balance < -1 and key < x.right.val:
            x.right = self.rotate_right(x.right)
            return self.rotate_left(x)

        return x

    def rotate_left(self, z):
        y = z.right
        u = y.left
        y.left = z
        z.right = u

        z.h = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.h = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        u = y.right
        y.right = z
        z.left = u

        z.h = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.h = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, x):
        if not x:
            return 0
        return x.h

    def get_balance(self, x):
        if not x:
            return 0
        return self.get_height(x.left) - self.get_height(x.right)

    def print_preorder(self, x):
        if not x:
            return
        print(x.val, end=" ")
        self.print_preorder(x.left)
        self.print_preorder(x.right)


t = AVL_Tree()
x = None
x = t.insert(x, 10)
x = t.insert(x, 20)
x = t.insert(x, 30)
x = t.insert(x, 40)
x = t.insert(x, 50)
x = t.insert(x, 25)

"""
        30
       /  \
     20   40
    /  \     \
   10  25    50
"""

t.print_preorder(x)


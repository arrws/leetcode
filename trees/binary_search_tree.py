class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.leftmost(root)

    def leftmost(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        # return the next smallest number
        x = self.stack.pop()
        if x.right:
            self.leftmost(x.right)
        return x.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


class BinarySearchTree:

    def isValid(self, root: TreeNode):
        def valid(root, mn, mx):
            if root == None:
                return True
            if mn < root.val < mx:
                return valid(root.left, mn, root.val) and valid(root.right, root.val, mx)
            return False
        return valid(root, float('-inf'), float('inf'))

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        p, q = min(p.val, q.val), max(p.val, q.val)
        while root:
            if root.val < p:
                root = root.right
            elif root.val > q:
                root = root.left
            else:
                return root
        return None

    def insertValue(self, root: TreeNode, v: int):
        if root.right and v > root.val:
            self.insertValue(root.right, v)
        elif root.left and v < root.val:
            self.insertValue(root.left, v)
        else:
            n = TreeNode(v)
            if v > root.val:
                root.right = n
            if v < root.val:
                root.left = n

    def kthElement(self, root: TreeNode, k: int):
        self.k = k
        def dive(root):
            if root == None:
                return None
            x = dive(root.left)
            if self.k == 0:
                return x
            self.k -= 1
            if self.k == 0:
                return root.val
            x = dive(root.right)
            if self.k == 0:
                return x
            return None
        return dive(root)


    def deleteNode(self, root, key):
        # using rotations

        if root == None:
            return root

        # find node and parent
        p = None
        x = root
        while x and x.val != key:
            p = x
            if x.val > key:
                x = x.left
            else:
                x = x.right

        # check if node exists
        if x == None:
            return root

        while x.right:
            u1 = x.right.left
            x.right.left = x
            u2 = x.right

            x.right = u1
            if p == None:
                # if key is root, reset the root
                root = u2
            else:
                if x == p.left:
                    p.left = u2
                else:
                    p.right = u2
            # reset parent node
            p = u2

        if p == None:
            # no rotation performed and key is root
            return x.left
        else:
            # after all rotation, key's right child is None
            if x == p.left:
                p.left = x.left
            else:
                p.right = x.left
            return root

    def deleteNode(self, root, key):

        if root == None:
            return root

        # find node and parent
        p = TreeNode(-1000)
        p.right = root
        x = root
        while x and x.val != key:
            p = x
            if x.val > key:
                x = x.left
            else:
                x = x.right

        # check if node exists
        if x == None:
            return root

        # if node is leaf
        if x.right == None and x.left == None:
            if p.right and p.right == x:
                p.right = None
            else:
                p.left = None

            # edgecase for root is the deleted node
            if p.right == None and p.left == None and p.val == -1000:
                return None
            return root

        # if node has only 1 child
        if x.left == None:
            x.val = x.right.val
            x.left = x.right.left
            x.right = x.right.right
            return root
        if x.right == None:
            x.val = x.left.val
            x.right = x.left.right
            x.left = x.left.left
            return root

        # if node has 2 children
        def getMin(x):
            # returns minimum succeding node and its parent
            p = x
            while x.left:
                p = x
                x = x.left
            return p, x

        py, y = succ(x.right)
        x.val = y.val
        # if the node to replace x is x.right (x == y.right)
        if py.val == y.val:
            x.val = y.val
            x.right = y.right
        else:
            # just delete y
            py.left = y.right
        return root



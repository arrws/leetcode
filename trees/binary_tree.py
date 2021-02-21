class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.depth = None
        self.parent = None

class BinaryTree:

    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = preorder.pop(0)
        i = inorder.index(root)
        x = TreeNode(root)
        x.left = self.buildTree(preorder, inorder[:i])
        x.right = self.buildTree(preorder, inorder[i+1:])
        return x

    def isSubtree(self, s: TreeNode, t: TreeNode):
        if s == None:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or  self.isSubtree(s.right, t)

    def isSameTree(self, p: TreeNode, q: TreeNode):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # def isValidBST(self, root: TreeNode) -> bool:
    #     def valid(root, mn, mx):
    #         if root == None:
    #             return True
    #         if mn < root.val < mx:
    #             return valid(root.left, mn, root.val) and valid(root.right, root.val, mx)
    #         return False
    #     return valid(root, float('-inf'), float('inf'))

    def invertTree(self, root: TreeNode):
        if root == None:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root

    def levelOrder(self, root: TreeNode):
        if not root: return []
        q = [root]
        r = []
        while len(q) > 0:
            u = []
            for _ in range(len(q)):
                x = q.pop(0)
                u.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            r.append(u)
        return r

    def maxPathSum(self, root: TreeNode):
        self.m = root.val

        def find(root):
            if root == None:
                return 0
            r = find(root.right)
            l = find(root.left)
            v = root.val + max([0, r, l])
            self.m = max([self.m, v, root.val + r + l])
            return v

        v = find(root)
        return max(self.m, v)


def lowest_common_ancestor(self, root, p:TreeNode, q:TreeNode):
    def process(root, d, p):
        root.depth = d
        root.parent = p
        if root.left != None:
            compute_depth(root.left, d+1, root)
        if root.right != None:
            compute_depth(root.right, d+1, root)

    process(root, 0, None)

    while p != None and p.depth > q.depth:
        p = p.parent
    while q != None and q.depth > p.depth:
        q = q.parent
    while p != None and q != None p != q:
        p = p.parent
        q = q.parent

    if p != None:
        return p
    return -1


def lowestCommonAncestor(self, root, p:int, q:int):
    # stupid version
    self.lca = None
    p, q = min(p.val, q.val), max(p.val, q.val)

    def dive(root):
        if root == None:
            return None

        # return value if matched otherwise None
        left = dive(root.left)
        right = dive(root.right)

        if root.val == p or root.val == q:
            u = p + q - root.val
            if left == u or right == u:
                self.lca = root
            return root.val
        else:
            if left != None and right != None:
                self.lca = root
            if left != None:
                return left
            return right

    dive(root)
    return self.lca


def lca_deepest_leaves(self, root):
        # return the LCA of the deepest leaves
        self.max_depth = -1
        self.lca = None

        def dive(root, prev_depth):
            if root == None:
                return -1

            depth = prev_depth + 1

            # if leaf update max_depth
            if root.left == None and root.right == None:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.lca = root
                return depth

            left_depth = dive(root.left, depth)
            right_depth = dive(root.right, depth)

            # left right leaves have highest depth
            if left_depth == right_depth == self.max_depth:
                self.lca = root

            return max(left_depth, right_depth)

        dive(root, -1)
        return self.lca



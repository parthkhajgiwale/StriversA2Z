class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # ---- Insert ----
    def insert(self, val):
        if self.root is None:
            self.root = BSTNode(val)
            return

        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = BSTNode(val)
                    return
                cur = cur.left
            elif val > cur.val:
                if cur.right is None:
                    cur.right = BSTNode(val)
                    return
                cur = cur.right
            else:
                return  # ignore duplicates

    # ---- Search ----
    def contains(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return True
            cur = cur.left if val < cur.val else cur.right
        return False

    # ---- Traversals ----
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.val)
        self._inorder(node.right, result)

    # ---- Min / Max ----
    def min(self):
        cur = self.root
        if cur is None:
            return None
        while cur.left:
            cur = cur.left
        return cur.val

    def max(self):
        cur = self.root
        if cur is None:
            return None
        while cur.right:
            cur = cur.right
        return cur.val

bst = BST()
bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(3)

print(bst.inorder())   # [1, 2, 3, 5, 8]
print(bst.contains(3))  # True
print(bst.min())        # 1
print(bst.max())        # 8

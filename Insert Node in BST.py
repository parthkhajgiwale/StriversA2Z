# Problem Statement:
# Given the root of a Binary Search Tree (BST) and a value `val`,
# insert `val` into the BST and return the root of the updated tree.
# It is guaranteed that `val` does not already exist in the BST.
#
# BST Property:
# - Left subtree contains values less than the node
# - Right subtree contains values greater than the node

# Approach:
# 1. If the tree is empty, create and return a new node with `val`.
# 2. Otherwise, compare `val` with the current node's value:
#    - If `val` is smaller, recursively insert into the left subtree.
#    - If `val` is larger, recursively insert into the right subtree.
# 3. Return the root node after insertion.
#
# Time Complexity: O(h), where h is the height of the tree
# Space Complexity: O(h) due to recursion stack

class Solution:
    def insertIntoBST(self, root, val):
        # Base case: if tree is empty, create a new node
        if root is None:
            return TreeNode(val)
        
        # If value is less than current node, go left
        if val < root.data:
            root.left = self.insertIntoBST(root.left, val)
        
        # If value is greater than current node, go right
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        # Return the unchanged root node
        return root

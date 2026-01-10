# Problem Statement:
# Given the root of a binary tree, check whether it is a valid
# Binary Search Tree (BST).
#
# A valid BST satisfies:
# 1. All values in the left subtree are strictly less than the node's value.
# 2. All values in the right subtree are strictly greater than the node's value.
# 3. Both left and right subtrees must also be valid BSTs.

# Approach:
# We use the concept of value ranges.
# Each node must lie within a valid range (min_val, max_val).
#
# - Initially, the range is (-infinity, +infinity).
# - For the left child, update the max range to current node's value.
# - For the right child, update the min range to current node's value.
#
# If any node violates this range, the tree is not a BST.
#
# Time Complexity: O(n), where n is the number of nodes
# Space Complexity: O(h), where h is the height of the tree (recursion stack)

class Solution:
    def isBST(self, root):
        
        def validate(node, min_val, max_val):
            # An empty tree is a valid BST
            if node is None:
                return True
            
            # Check if current node violates the BST property
            if not (min_val < node.data < max_val):
                return False
            
            # Recursively validate left and right subtrees
            return (validate(node.left, min_val, node.data) and
                    validate(node.right, node.data, max_val))
        
        # Start validation with infinite bounds
        return validate(root, float('-inf'), float('inf'))

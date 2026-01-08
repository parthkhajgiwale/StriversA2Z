# ----------------------------------------------------
# Problem:
# Given a Binary Search Tree (BST), find its maximum height.
#
# The height of a binary tree is defined as the number of
# nodes on the longest path from the root node to any leaf node.
#
# ----------------------------------------------------
# Approach:
# 1. Create a BST by inserting nodes following BST rules.
# 2. To find the height:
#    - If the current node is NULL, return 0.
#    - Recursively find the height of the left subtree.
#    - Recursively find the height of the right subtree.
#    - The height of the tree is:
#        max(left subtree height, right subtree height) + 1
# ----------------------------------------------------


# Class to represent a node in the BST
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to insert a value into the BST
def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


# Function to calculate the maximum height of the BST
def max_height(root):
    # Base case: if tree is empty, height is 0
    if root is None:
        return 0

    # Recursively calculate height of left and right subtrees
    left_height = max_height(root.left)
    right_height = max_height(root.right)

    # Return the maximum of both heights plus 1 (for current node)
    return max(left_height, right_height) + 1


# ------------------- Main Program -------------------

# Create BST
root = None
values = [10, 5, 15, 2, 7]

for value in values:
    root = insert(root, value)

# Print maximum height of BST
print("Maximum height of BST:", max_height(root))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = []
        curr = root
        
        # Standard iterative inorder traversal
        while curr or stack:
            # 1) Go as left as possible, pushing nodes on the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2) Visit the next node in inorder (smallest remaining)
            curr = stack.pop()
            k -= 1  # We visited one more smallest element
            
            # 3) If this is the kth visited, it's the answer
            if k == 0:
                return curr.val
            
            # 4) Move to the right subtree (next larger values)
            curr = curr.right
        
        # If k is invalid (shouldn't happen with valid input)
        return -1

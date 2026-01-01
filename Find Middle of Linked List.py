# Question:
# Given the head of a singly linked list, return the middle node.
# If the list has an even number of nodes, return the second middle node.

# Example:
# Input: head -> 3 -> 8 -> 1 -> 7 -> 0
# Output: Node with value 1 (middle of the list)
# Explanation: There are 5 nodes, so the 3rd node (value 1) is the middle.

# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleOfLinkedList(self, head):
        slow = head        # slow pointer moves 1 step at a time
        fast = head        # fast pointer moves 2 steps at a time

        # Move until fast reaches end
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow        # slow is now at the middle node

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findStartingPoint(self, head):
        """
        Finds the starting point of a loop in a singly linked list.
        If no loop exists, returns None.
        """

        # Edge case: empty list or single node without loop
        if not head or not head.next:
            return None

        # Step 1: Detect cycle using slow and fast pointers
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next          # move one step
            fast = fast.next.next    # move two steps

            # Cycle detected
            if slow == fast:
                break
        else:
            # If we exit the loop normally, no cycle exists
            return None

        # Step 2: Find the starting point of the loop
        slow = head  # move slow to head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Both pointers now point to the start of the loop
        return slow

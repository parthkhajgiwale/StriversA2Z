# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head):
        """
        Problem:
        Given the head of a singly linked list, determine if the linked list
        contains a cycle (loop).

        A cycle exists if by continuously following the 'next' pointer,
        we can reach a node that has already been visited.

        Approach:
        Use Floyd’s Cycle Detection Algorithm (Tortoise and Hare).

        - Use two pointers:
          1. slow pointer moves one step at a time
          2. fast pointer moves two steps at a time

        - If there is a cycle, fast and slow will eventually meet.
        - If there is no cycle, fast will reach the end (None).

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Initialize both pointers at the head
        slow = head
        fast = head

        # Traverse the linked list
        while fast and fast.next:
            # Move slow by one step
            slow = slow.next

            # Move fast by two steps
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # If fast reaches None, no cycle exists
        return False

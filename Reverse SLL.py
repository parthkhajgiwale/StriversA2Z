class Solution:
    def reverseList(self, head):
        """
        Reverses a singly linked list and returns the new head.
        """

        prev = None        # Will become the new head
        curr = head        # Start from the original head

        while curr:
            next_node = curr.next   # Store next node
            curr.next = prev        # Reverse the link
            prev = curr             # Move prev forward
            curr = next_node        # Move curr forward

        # prev is the new head after reversal
        return prev

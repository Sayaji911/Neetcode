from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        """
        Definition for singly-linked list node.
        """
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a given linked list in-place.

        The function takes a linked list and reorders it by moving the last node to the second position,
        the second-to-last node to the third position, and so on.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.

        Returns:
        - None: The function modifies the linked list in-place and does not return anything.

        Algorithm:
        1. Find the middle node of the linked list using the slow and fast pointer technique.
        2. Reverse the second part of the linked list starting from the middle node.
        3. Swap elements between the first and reversed second part to reorder the list.
        """

        # Step 1: Find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second part of the linked list
        second = slow.next
        prev = slow.next
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Step 3: Swap elements between the first and reversed second part
        first, second = head, prev
        while second:
            fnext, snext = first.next, second.next
            first.next = second
            second.next = fnext
            first, second = fnext, snext

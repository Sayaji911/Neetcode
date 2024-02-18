from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify handling the head of the merged list
        dummy = node = ListNode()

        # Loop until either list1 or list2 becomes empty
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val > list2.val:
                # If the value in list2 is smaller, append it to the merged list
                node.next = list2
                # Move to the next node in list2
                list2 = list2.next
            else:
                # If the value in list1 is smaller or equal, append it to the merged list
                node.next = list1
                # Move to the next node in list1
                list1 = list1.next

            # Move to the next node in the merged list
            node = node.next

        # Connect the remaining nodes from either list1 or list2
        node.next = list1 or list2

        # Return the merged list starting from the next node of the dummy node
        return dummy.next

# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        lists = [[1,4,5] , [1,3,4], [2,6]]
        OP = [1,2,3,4,5,6]
        """

        if not lists or not len(lists):
            return

        merged_list = []
        while len(lists) > 1:
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.merge_two_list(l1, l2))
            lists = merged_list
        return lists[0]

    def merge_two_list(self, l1: ListNode, l2: ListNode):
        tail = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next


def list_to_linked_list(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Create linked lists for each sublist
list1 = list_to_linked_list([1, 3])
list2 = list_to_linked_list([2, 4])
# list3 = list_to_linked_list([2, 6])

# Assemble the input list of linked lists
test_input = [list1, list2]


obj = Solution()

print(obj.mergeKLists(lists=test_input))

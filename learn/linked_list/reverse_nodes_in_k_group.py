from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        groupPrev = dummy

        while True:
            kth = self.catch_kth_node(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

    def catch_kth_node(self, head: ListNode, k: int) -> ListNode:
        for i in range(0, k):
            head = hea t5 xd.next
        return head

    def display(self, head):
        current = head

        print("---")
        while current:
            print(current.value, end=" <-> ")
            current = current.next

        print("None")


def list_to_linked_list(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


# Create linked lists for each sublist
list1 = list_to_linked_list([1, 2, 3, 4, 5])
# list2 = list_to_linked_list([2, 4])
# list3 = list_to_linked_list([2, 6])

# Assemble the input list of linked lists
test_input = list1


obj = Solution()

print(obj.reverseKGroup(head=test_input, k=2))

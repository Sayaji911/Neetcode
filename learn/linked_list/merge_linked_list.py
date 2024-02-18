from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge_two_lists(self, list1: ListNode, list2: ListNode):
        if not list1 and not list2:
            return
        elif not list2:
            return list1
        elif not list1:
            return list2

        if list1.val < list2.val:
            tmp1 = list1.next = self.merge_two_lists(list1.next, list2)
            
            return list1
        else:
            tmp2 = list2.next = self.merge_two_lists(list2.next, list1)
            return list2
        
        '''
        merge_two_lists([1,3], [2,4])
        mergeTwoLists(3,2)
        mergeTwoLists(3,4)
        4=mergeTwoLists(4)
        '''
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return

        elif len(lists) == 1:
            return lists[0]

        elif len(lists) == 2:
            return self.merge_two_lists(list1, list2)
        mid = len(lists) // 2

        right = lists[mid:]
        left = lists[:mid]

        return self.merge_two_lists(self.mergeKLists(left), self.mergeKLists())

        
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


"""
[[1,3],[2,4]]

l1.val = 1 < l2.val = 2
    mergeTwoLists(3,2)
l1.val = 3 > l2.val = 2
    mergeTwoLists(3,4)
l1.val = 3 < l2.val = 4
    mergeTwoLists(4)

elif not list1:
    return list2

4

"""

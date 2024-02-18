# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        

        count = {}

        cur = head

        while cur:
            if cur.next:
                if cur in count:
                    return True
                else:
                    count[cur] = cur.val
                cur = cur.next

        return False

def hasCycle2(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    
    while fast.next != None and fast != None:
        slow = slow.next
        fast = fast.next
    
        if slow == fast:
            return True
        
    return False
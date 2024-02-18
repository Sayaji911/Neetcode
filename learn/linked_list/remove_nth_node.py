from typing import Optional

class ListNode:
    pass


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    
    slow = dummy
    fast = head
    
    while n > 0:
        fast = fast .next
        n = n - 1

    while fast:
        slow = slow.next
        fast = fast.next
        
    slow.next = slow.next.next
    
    return dummy.next
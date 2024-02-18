def copyRandomList(self, head: "Node") -> "Node":
    """
    Copies a linked list with nodes having 'val', 'next', and 'random' pointers.

    The function creates a deep copy of the given linked list by iterating through
    the original list twice. During the first pass, it creates new nodes and maps
    each original node to its corresponding copy in a hash map. In the second pass,
    it assigns the 'next' and 'random' pointers for each copied node using the hash map.

    Parameters:
    - head ("Node"): The head of the original linked list.

    Returns:
    - "Node": The head of the newly created deep copy of the linked list.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    oldToCopy = {None: None}

    cur = head
    # First pass: Create new nodes and populate the hash map
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
    
    cur = head
    # Second pass: Assign 'next' and 'random' pointers for each copied node
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    
    return oldToCopy[head]

class DoubleNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self, value) -> None:
        self.head = DoubleNode(value=value)
        self.length = 1
        self.tail = self.head

    def append(self, value) -> None:
        new_node = DoubleNode(value=value)
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")
        print(self.length)

    def insert(self, index, value):
        new_node = DoubleNode(value=value)
        if index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.length += 1

            return

        leader = self.traverse_linked_list(index - 1)

        new_node.previous = leader
        new_node.next = leader.next
        leader.next.previous = new_node
        leader.next = new_node
        self.length += 1

    def traverse_linked_list(self, index):
        current_node = self.head
        for i in range(index):
            if current_node.next:
                current_node = current_node.next
            else:
                return "No such index"
        return current_node

    def remove(self, value):
        current_node = self.head

        if self.head.value == value:
            self.head = self.head.next

        while current_node.next and current_node.next.value != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next
            current_node.next.next.previous = current_node

        self.length -= 1

    def reverse(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            current.previous = next
            prev = current
            current = next

        self.head = prev


mLinkedList = DoublyLinkedList(10)
mLinkedList.append(20)
mLinkedList.append(30)
mLinkedList.append(40)
mLinkedList.append(50)
mLinkedList.append(60)
mLinkedList.insert(0, 5)
mLinkedList.insert(3, 25)
mLinkedList.remove(5)
mLinkedList.remove(40)
mLinkedList.reverse()

mLinkedList.display()

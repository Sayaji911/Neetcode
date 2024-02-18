

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value) -> None:
        self.head = Node(value=value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value=value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return (self.length,)

    def prepend(self, value):
        new_node = Node(value=value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete(self, value):
        current_node = self.head

        if self.head.value == value:
            self.head = self.head.next

        while current_node.next and current_node.next.value != value:
            current_node = current_node.next

        if current_node.next:
            current_node.next = current_node.next.next

    def insert(self, index, value):
        new_node = Node(value=value)

        current_node = self.head
        i = 0
        if index == 0:
            new_node.next = self.head
            self.head = new_node

            return

        while (i + 1) != index:
            current_node = current_node.next
            i += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def remove(self, index):
        current_node = self.head
        i = 0
        if index == 0:
            self.head = current_node.next
            return

        while (i + 1) != index:
            current_node = current_node.next
            i += 1

        current_node.next = current_node.next.next


# mLinkedList = LinkedList(10)
# mLinkedList.append(20)
# mLinkedList.prepend(5)
# mLinkedList.display()
# print("-----------")
# # mLinkedList.delete(10)
# # mLinkedList.display()
# mLinkedList.insert(1, 7)
# mLinkedList.display()
# mLinkedList.insert(0, 1.1)
# mLinkedList.display()
# mLinkedList.remove(0)
# mLinkedList.display()
# mLinkedList.remove(1)
# mLinkedList.display()
# mLinkedList.remove(2)
# mLinkedList.display()


# print(mLinkedList.head)

# Author: Melissa Perez
# Date: --/--/--
# Description:

class MyLinkedList:
    class Node:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.front = self.Node()
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.front.next
        curr_index = 0

        if self.length - 1 < index:
            return -1

        while curr is not None and curr_index < index:
            curr_index += 1
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = self.Node(val)
        new_head.next = self.front.next
        self.front.next = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.front.next

        if curr is None:
            self.addAtHead(val)
            return

        while curr.next is not None:
            curr = curr.next

        new_tail = self.Node(val)
        new_tail.next = curr.next
        curr.next = new_tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev, curr = self.front, self.front.next
        curr_index = 0

        if index > self.length:
            return

        while curr is not None and curr_index < index:
            prev = prev.next
            curr = curr.next
            curr_index += 1

        if self.length == index:
            self.addAtTail(val)
            return
        else:
            node_to_insert = self.Node(val)
            node_to_insert.next = curr
            prev.next = node_to_insert
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        prev, curr = self.front, self.front.next
        curr_index = 0

        while curr is not None and curr_index < index:
            curr_index += 1
            curr = curr.next
            prev = prev.next

        if curr_index > self.length - 1:
            return

        prev.next = curr.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
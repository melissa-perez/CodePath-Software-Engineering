# Author: Melissa Perez
# Date: --/--/--
# Description:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        links = self.getLength(head) - 1
        num = 0

        while head is not None:
            num += (2 ** links) * head.val
            links -= 1
            head = head.next

        return num

    def getLength(self, head):
        current_node = head
        ll_length = 0

        while current_node is not None:
            ll_length += 1
            current_node = current_node.next

        return ll_length
 
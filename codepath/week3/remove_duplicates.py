# Author: Melissa Perez
# Date: --/--/--
# Description:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if not head:
            return head

        current_node = next_unique_node = head

        while next_unique_node is not None:
            if next_unique_node.val != current_node.val:
                current_node.next = next_unique_node
                current_node = current_node.next
            next_unique_node = next_unique_node.next

        current_node.next = None

        return head

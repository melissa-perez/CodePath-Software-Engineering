# Author: Melissa Perez
# Date: --/--/--
# Description:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        front = ListNode(next=head)

        end = front.next
        curr = end.next

        while curr is not None:
            end.next = curr.next
            curr.next = front.next
            front.next = curr

            curr = end.next

        return front.next
# Author: Melissa Perez
# Date: --/--/--
# Description:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        front = ListNode(next=head)
        prev = front
        delayed = curr = front.next
        index_steps = 0

        while curr is not None:

            while curr is not None and index_steps < n:
                curr = curr.next
                index_steps += 1

            if curr is not None:
                curr = curr.next
                delayed = delayed.next
                prev = prev.next

        prev.next = delayed.next

        return front.next
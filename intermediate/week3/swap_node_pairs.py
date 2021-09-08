# Author: Melissa Perez
# Date: --/--/--
# Description:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if not head:
            return head

        front = ListNode(next=head)
        prev, curr, runner = front, front.next, front.next.next

        while curr is not None and runner is not None:
            # perform the switch
            curr.next = runner.next
            runner.next = curr
            prev.next = runner

            # updates the pointers
            prev = curr
            curr = curr.next

            if curr is not None:
                runner = curr.next

        return front.next
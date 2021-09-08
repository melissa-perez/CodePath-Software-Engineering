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

        front = ListNode(val=-102, next=head)
        curr, runner = front.next, front.next.next

        while runner is not None and curr is not None:

            if runner.val != curr.val:
                runner = runner.next
                curr = curr.next
            else:

                while runner is not None and runner.val == curr.val:
                    runner = runner.next

                curr.next = runner
                curr = curr.next

                if runner is not None:
                    runner = runner.next

        return front.next

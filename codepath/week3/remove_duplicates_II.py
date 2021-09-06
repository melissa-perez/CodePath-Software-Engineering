# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        front = ListNode(val=-102, next=head)
        prev, curr, runner = front, front.next, front.next.next

        while curr is not None and curr.next is not None:
            if curr.val != prev.val and curr.val != runner.val:
                curr = curr.next
                prev = prev.next
                runner = runner.next
            else:
                while runner is not None and curr.val == runner.val:
                    runner = runner.next
                prev.next = runner
                curr = runner
                if curr is not None:
                    runner = runner.next
        return front.next

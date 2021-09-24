# Author: Melissa Perez
# Date: --/--/--
# Description:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Need the length of the list for this problem
        # Need to calculate only the new_head_index: (n - k) % n

        if not head or not head.next:
            return head

        # need to find the old tail
        ll_length = self.get_length(head)
        index = 1
        old_tail = head
        front = ListNode(next=head)

        while index < ll_length:
            old_tail = old_tail.next
            index += 1

        # need to find the new head and new tail
        new_head_loc = (ll_length - k) % ll_length
        new_tail, new_head = front, front.next

        for i in range(new_head_loc):
            new_tail = new_tail.next
            new_head = new_head.next

        new_tail.next = old_tail.next
        old_tail.next = front.next
        front.next = new_head

        return front.next

    def get_length(self, head):
        curr = head
        length = 0

        while curr is not None:
            curr = curr.next
            length += 1

        return length
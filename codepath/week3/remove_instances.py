# Author: Melissa Perez
# Date: --/--/--
# Description:


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        front = ListNode(next=head)
        prev, curr = front, front.next

        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return front.next
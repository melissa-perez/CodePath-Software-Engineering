# Author: Melissa Perez
# Date: --/--/--
# Description:

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle_pos = self.getLength(head) // 2
        index = 0

        while index < middle_pos:
            index += 1
            head = head.next

        return head

    def getLength(self, head):

        ll_length = 0
        current = head

        while current is not None:
            ll_length += 1
            current = current.next
        return ll_length
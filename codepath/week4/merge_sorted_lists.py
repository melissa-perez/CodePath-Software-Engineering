# Author: Melissa Perez
# Date: --/--/--
# Description:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_runner = l1
        l2_runner = l2
        sort_list = ListNode()
        sort_list_runner = sort_list

        while l1_runner is not None or l2_runner is not None:
            if l1_runner is None or l2_runner is not None and l1_runner.val > l2_runner.val:
                sort_list_runner.next = l2_runner
                l2_runner = l2_runner.next
            elif l2_runner is None or l1_runner is not None and l1_runner.val <= l2_runner.val:
                sort_list_runner.next = l1_runner
                l1_runner = l1_runner.next
            sort_list_runner = sort_list_runner.next

        return sort_list.next

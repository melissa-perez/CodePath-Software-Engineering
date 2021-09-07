# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:          
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        less_runner = less
        more = ListNode()
        more_runner = more
        
        while head is not None:
            if head.val < x:
                less_runner.next = head
                less_runner = less_runner.next
            elif head.val >= x:
                more_runner.next = head
                more_runner = more_runner.next

            head = head.next

        more_runner.next = None
        less_runner.next = more.next     
        head = less.next

        return head

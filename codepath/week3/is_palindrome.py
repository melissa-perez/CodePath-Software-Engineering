# Author: Melissa Perez
# Date: --/--/--
# Description:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        Go through list and add it to array
        Key will be index
        Afterwards, do two pointer
        one at start
        one at end
        go towards middle
        if middle is reached
        it is a palindrom
        else not

        """
        # always check if head is valid
        if head is None:
            return

        list_of_nodes = []
        current_node = head
        while current_node is not None:
            list_of_nodes.append(current_node.val)
            current_node = current_node.next

        start = 0
        end = len(list_of_nodes) - 1

        while start < end:
            if list_of_nodes[start] != list_of_nodes[end]:
                return False
            start += 1
            end -= 1
        return True
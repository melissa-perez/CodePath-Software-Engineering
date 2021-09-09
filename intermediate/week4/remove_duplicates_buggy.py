# Author: Melissa Perez
# Date: --/--/--
# Description:

#
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# Input : 1 ; Output : 1
# Input : 1->1 ; Output: 1
# Input : 1->1->1->2->2 ; Output: 1->2
#
class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def equals(self, n):
        if (self.data != n.data):
            return False

        if (self.next == None):
            if (n.next != None):
                return False
            else:
                return True

        return ListNode.equals(self.next, n.next)


def removeDuplicates(head):
    if head is not None and head.next is not None:
        dummy = head

        while dummy is not None and dummy.next is not None:
            if dummy.data == dummy.next.data:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return head
    return head


class Main:
    if __name__ == '__main__':
        n1_1 = ListNode(1)
        print("Test cases 1 passed: " + str(removeDuplicates(n1_1).equals(n1_1)))

        n2_1a = ListNode(1)
        n2_1b = ListNode(1)
        n2_1a.next = n2_1b

        n2_answer = ListNode(1)
        print("Test case 2 passed: " + str(removeDuplicates(n2_1a).equals(n2_answer)))

        n3_1a = ListNode(1)
        n3_1b = ListNode(1)
        n3_2a = ListNode(2)
        n3_2b = ListNode(2)
        n3_1a.next = n3_1b
        n3_1b.next = n3_2a
        n3_2a.next = n3_2b

        n3_answer1 = ListNode(1)
        n3_answer2 = ListNode(2)
        n3_answer1.next = n3_answer2

        print("Test case 3 passed: " + str(removeDuplicates(n3_1a).equals(n3_answer1)))

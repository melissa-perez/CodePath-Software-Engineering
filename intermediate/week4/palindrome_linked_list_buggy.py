# Author: Melissa Perez
# Date: --/--/--
# Description:

#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true

# Testing

class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def isPalindrome(node):
    fullLength = getLength(node)

    firstHalf = [None] * (fullLength // 2)  # this is in an array || needs to be initialized
    currentNode = 0

    while currentNode < (fullLength // 2):
        firstHalf[currentNode] = node.data
        node = node.next
        currentNode += 1

    if fullLength % 2 != 0:
        node = node.next

    while (node is not None and currentNode > 0):
        if (node.data != firstHalf[currentNode - 1]):
            # changed currentNode to currentNode - 1, out of index
            return False
        node = node.next
        currentNode -= 1

    return True


def getLength(node):
    length = 0

    while (node is not None):
        length += 1
        node = node.next

    return length


class Main:
    if __name__ == '__main__':
        n1_1 = ListNode(1)
        print("Test cases 1 passed: " + str(isPalindrome(n1_1)))

        n2_1 = ListNode(1)
        n2_2 = ListNode(2)
        n2_1.next = n2_2
        print("test case 2 passed: " + str(not isPalindrome(n2_1)))

        n3_1 = ListNode(1)
        n3_2 = ListNode(2)
        n3_3 = ListNode(3)
        n3_1.next = n3_2
        n3_2.next = n3_3
        print("test case 3 passed: " + str(not isPalindrome(n3_1)))

        n4_1 = ListNode(1)
        n4_2 = ListNode(2)
        n4_3 = ListNode(1)
        n4_1.next = n4_2
        n4_2.next = n4_3
        print("test case 4 passed: " + str(isPalindrome(n4_1)))

        n4_1 = ListNode(1)
        n4_2 = ListNode(2)
        n4_3 = ListNode(1)
        n4_4 = ListNode(1)
        n4_1.next = n4_2
        n4_2.next = n4_3
        n4_3.next = n4_4
        print("test case 5 passed: " + str(not isPalindrome(n4_1)))

        n4_1 = ListNode(1)
        n4_2 = ListNode(2)
        n4_3 = ListNode(2)
        n4_4 = ListNode(1)
        n4_1.next = n4_2
        n4_2.next = n4_3
        n4_3.next = n4_4
        print("test case 6 passed: " + str(isPalindrome(n4_1)))
# Linked List I
## Session 1

### Palindrome
Given a linked list, determine if it is a palindrome. Your method would take in a linked list and return True / False for whether the list is a palindrome or not.

Note: A palindrome is a word, phrase, or sequence that reads the same backwards as forwards (i.e "mom", "racecar", "1221").

### Detect Cycle
Given a linked list, determine if it has a cycle in it. For this problem, it may be helpful for you to write some pseudocode on how to build a linked list with a cycle.

### Remove Instances
Given a linked list and a value x, remove all instances of x from the linked list

### Partition
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

## Session 2

### Remove Duplicates I
Given a sorted linked list, delete all duplicates such that each element appear only once.

###  Linked List Cycle
Given a linked list, determine if it has a cycle in it. For simplicity, assume the linked list cannot have more than 1000 nodes in it.

### Merge Two Sorted Lists
Merge two sorted linked lists.


### Remove Duplicates II

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

## Post-Session Assignments

### Design a Linked List
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index-th node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


### Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.


### Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

### Merge Two Sorted Lists
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

### Swap Node Pairs
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

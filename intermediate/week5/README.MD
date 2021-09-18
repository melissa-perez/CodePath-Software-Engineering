# Review

## Session 1

### Word Frequency
Implement a method to find the number of occurrences of any given word in a book. A word is represented as a string and a book is represented as an array / list of strings.

Optimize the method to be called multiple times.

### Reverse a Doubly Linked List
Given a doubly linked list containing n nodes. The problem is to reverse every group of k nodes in the list.

### Count Triplet Sums

Given a sorted doubly linked list of distinct nodes (i.e. no two nodes have the same data), count triplets in the list that sum up to a given value x.

## Session 2

### Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.

Note: Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

### Intersection of Arrays
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

### Next Greater Node
We are given a linked list with head as the first node. Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice. If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

## Post-Session Assignments

### Next Greater Node
You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

### Merge K-sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

### Flatten a Multi-Level Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

### Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

### Merge Intervals

Given an array of intervals where intervals`[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Count distinct elements in every window of size k

Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k. 

### Find the Length of the largest subarray with sum 0

Given an array of integers, find the length of the longest sub-array with a sum that equals 0.

### Print all subarrays with sum 0

Given an array, print all subarrays in the array which has sum 0.

### Find if a binary tree is balanced

Given a binary tree, Find whether if a Given Binary Tree is Balanced?

### Diameter of a binary tree

Given a binary tree, write an algorithm to find the diameter of the tree.

### Search a 2D matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

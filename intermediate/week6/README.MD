# Stacks and Queues

## Session 1


### Evaluate Postfix expression
Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators '+', '*', '-' and '/'.

Note: Arithmetic Expressions can be written in Infix, Prefix or Postfix notations.

### Valid Parenthesis
Given a string s containing characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

### Sort a stack using a temporary stack (bonus)
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).

The stack supports the following operations : push, pop, peek, isEmpty.


## Session 2

### Queue using Stacks
We are given a stack data structure that supports standard operations like (push, pop, peek, and empty), implement a queue using instances of stack data structure and operations on them.

Implement a Queue class with the following methods:

- void push(int x): Pushes element x to the back of the queue.
- int pop(): Removes the element from the front of the queue and returns it.
- int peek(): Returns the element at the front of the queue.
- boolean empty(): Returns true if the queue is empty, false otherwise.


### Stack Using Queues
Given a Queue data structure that supports standard operations like push, top, pop, and empty. Implement a Stack data structure using only instances of Queue and queue operations allowed on the instances.

Implement a Stack class:

- void push(int x): Pushes element x to the top of the stack.
- int pop(): Removes the element on the top of the stack and returns it.
- int top(): Returns the element on the top of the stack.
- boolean empty(): Returns true if the stack is empty, false otherwise.
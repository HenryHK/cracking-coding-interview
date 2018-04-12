#!/usr/bin/python3
# Idea: two pointer, a slow one and a fast one, the fast one will reach the slow one at the end.
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    slow = head
    fast = head
    if head == None:
        return 0
    else:
        while (head.next != None and head.next.next != None):
            slow = head.next
            fast = head.next.next
            if (slow.data == fast.data and slow.next == fast.next):
                return 1
        return 0

#!/usr/bin/python3
# Idea: top-down checking all nodes satisfy requirements
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

import sys


def check(root, min, max):
    if root == None:
        return True
    if root.data <= min or root.data >= max:
        return False
    return check(root.left, min, root.data) and check(root.right, root.data, max)


def check_binary_search_tree_(root):
    return check(root, float('-inf'), float('inf'))

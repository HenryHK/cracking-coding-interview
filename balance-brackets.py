#!/usr/bin/python3
# Idea: use a stack to store and pop it out when there is a match


def is_matched(expression):
    stack = []
    for c in expression:
        if c == '{' or c == '(' or c == '[':
            stack = [c] + stack
        else:
            if len(stack) == 0:
                return False
            if c == '}':
                if stack.pop(0) != '{':
                    return False
            if c == ')':
                if stack.pop(0) != '(':
                    return False
            if c == ']':
                if stack.pop(0) != '[':
                    return False
    if len(stack) == 0:
        return True
    else:
        return False


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

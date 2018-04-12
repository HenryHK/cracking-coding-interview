#!/usr/bin/python3
# Idea: use two stacks to implement a queue
# Notice: use PyPy to avoid over time


class MyQueue(object):
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def peek(self):
        if len(self.stack_2) == 0:
            for i in self.stack_1:
                self.stack_2 = [i] + self.stack_2
            self.stack_1.clear()
        return self.stack_2[0]

    def pop(self):
        if len(self.stack_2) == 0:
            for i in self.stack_1:
                self.stack_2 = [i] + self.stack_2
            self.stack_1.clear()
        self.stack_2.pop(0)

    def put(self, value):
        self.stack_1 = [value] + self.stack_1


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

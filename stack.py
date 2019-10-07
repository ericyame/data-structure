#!/usr/bin/python

class Stack():
    def __init__(self, items=[]):
        self.stack = list()
        self.stack.extend(items)

    def push(self, item):
        self.stack.append(item)

    def popItem(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def isEmpty(self):
        return (len(self.stack) == 0)

    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def getStack(self):
        return str(self.stack)

    def getSize(self):
        return len(self.stack)

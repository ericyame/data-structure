#!/usr/bin/python

from collections import deque 

class Queue():
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            self.queue.popleft()
        else:
            print("Queue is empty")

    def front(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def isEmpty(self):
        return len(self.queue) == 0

    def getQueue(self):
        return list(self.queue)

    def getSize(self):
        return len(self.queue)

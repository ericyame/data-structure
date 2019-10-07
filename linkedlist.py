#!/usr/bin/python

class Node():
    def __init__(self, item=0, node=None):
        self.item = item
        self.next = node

class Linkedlist():
    def __init__(self):
        self.front = None
        self.rear = None

    def addItemBack(self, item):
        node = Node(item)
        if self.front is None:
            self.front = node
        if self.rear is not None:
            self.rear.next = node
        self.rear = node

    def addItemFront(self, item):
        node = Node(item)
        node.next = self.front
        if self.rear is None:
            self.rear = node
        self.front = node

    def addItemAt(self, item, pos):
        if pos > self.getSize():
            print("The length of linked list is only "+ str(self.getSize()))
            return
        if pos == 0:
            self.addItemFront(item)
            return
        elif pos == self.getSize():
            self.addItemBack(item)
            return

        node = Node(item)
        current = self.front

        while pos - 1 > 0:
            current = current.next
            pos -= 1

        node.next = current.next
        current.next = node

    def removeItem(self, item):
        previous = None
        current = self.front

        dummyHead = Node(0)
        dummyHead.next = self.front
        previous = dummyHead
        current = dummyHead.next

        while current != None:
            if current.item == item:
                if current.next == None: # Item in last node
                    self.rear = previous
                    self.rear.next = None
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next
        self.front = dummyHead.next

        if self.getSize() == 0 and self.front is not None and self.rear is not None:
            self.front = None
            self.rear = None

    def searchItem(self, item):
        previous = None
        current = self.front

        while (current != None):
            if (current.item == item):
                print("Found " + str(item) + " in Linkedlist")
                return
            else:
                previous = current
            current = current.next
        print(str(item) + " is not in Linkedlist")

    def getLinkedlist(self):
        print("Size: " + str(self.getSize()))
        if (self.front is not None) and (self.rear is not None):
            print("Front: " + str(self.front.item))
            print("Rear: " + str(self.rear.item))
        else:
            print("Linkedlist is empty")
        current = self.front
        while (current != None):
            print(str(current.item), end='->')
            current = current.next
        print("None")

    def getSize(self):
        count = 0
        previous = None
        current = self.front

        while (current != None):
            count += 1
            previous = current
            current = current.next
        return count

    def reverse(self):
        if self.front is None:
            print("Linked list is empty")
            return

        print("Original linked list:")
        self.getLinkedlist()

        p = None
        q = self.front
        r = self.front.next

        while r is not None:
            q.next = p
            p = q
            q = r
            r = r.next
        q.next = p

        temp = self.front
        self.front = self.rear
        self.rear = temp

        print("Reversed linked list:")
        self.getLinkedlist()

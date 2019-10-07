from stack import Stack
from queue import Queue
from linkedlist import Linkedlist
from circularlinkedlist import CircularLinkedlist

print("Create Stack")
stack = Stack()
stack.popItem()
print("push(1)")
stack.push(1)
print("push(100)")
stack.push(100)
print("push(1000)")
stack.push(1000)
print("push(10000)")
stack.push(10000)
print("Stack top is: " + str(stack.top()) + ", Size is: " + str(stack.getSize()))
print("Stack: " + str(stack.getStack()))
print("Pop " + str(stack.popItem()) + ", Stack top is: " + str(stack.top()) + ", Size is: " + str(stack.getSize()))
print("Stack: " + str(stack.getStack()))

print("################\n")

print("Create Queue")
queue = Queue()
print("Queue is empty? " + str(queue.isEmpty()))
print("enqueue(1)")
queue.enqueue(1)
print("enqueue(100)")
queue.enqueue(100)
print("enqueue(1000)")
queue.enqueue(1000)
print("enqueue(10000)")
queue.enqueue(10000)
print("Queue: " + str(queue.getQueue()))
print("Queue is empty? " + str(queue.isEmpty()))
print("Dequeue")
queue.dequeue()
print("Queue front is: " + str(queue.front()) + ", Size is: " + str(queue.getSize()))
print("Queue: " + str(queue.getQueue()))
print("Dequeue")
queue.dequeue()
print("Queue front is: " + str(queue.front()) + ", Size is: " + str(queue.getSize()))
print("Queue: " + str(queue.getQueue()))

print("################\n")

print("Create Linked List")
l = Linkedlist()

print("addItemBack(1)")
l.addItemBack(1)
l.getLinkedlist()

print("addItemBack(2)")
l.addItemBack(2)
l.getLinkedlist()

print("addItemFront(3)")
l.addItemFront(3)
l.getLinkedlist()

print("addItemAt(4,2)")
l.addItemAt(4,2)
l.getLinkedlist()

print("searchItem(4)")
l.searchItem(4)

print("searchItem(5)")
l.searchItem(5)

print("reverse()")
l.reverse()

print("removeItem(2)")
l.removeItem(2)
l.getLinkedlist()

print("removeItem(3)")
l.removeItem(3)
l.getLinkedlist()

print("removeItem(4)")
l.removeItem(4)
l.getLinkedlist()

print("removeItem(1)")
l.removeItem(1)
l.getLinkedlist()

print("################\n")

print("Create Circular Linked List")
cl = CircularLinkedlist()

print("addItemBack(1)")
cl.addItemBack(1)
cl.getLinkedlist()

print("addItemBack(2)")
cl.addItemBack(2)
cl.getLinkedlist()

print("addItemFront(3)")
cl.addItemFront(3)
cl.getLinkedlist()

print("addItemAt(4,2)")
cl.addItemAt(4,2)
cl.getLinkedlist()

print("searchItem(4)")
cl.searchItem(4)

print("searchItem(5)")
cl.searchItem(5)

print("reverse()")
cl.reverse()

print("removeItem(2)")
cl.removeItem(2)
cl.getLinkedlist()

print("removeItem(3)")
cl.removeItem(3)
cl.getLinkedlist()

print("removeItem(4)")
cl.removeItem(4)
cl.getLinkedlist()

print("removeItem(1)")
cl.removeItem(1)
cl.getLinkedlist()
__author__ = 'Nimish'
''' QUEUE IMPLEMENTATION
        A Queue is a FIFO
        PUSH from one end(rear) and POP from other(front)
        Queue(): creates empty queue
        enqueue(item): Adds an item to the rear of the queue
        dequeue(): Removes the front item from the queue
        isEmpty(): Checks if the queue is empty
        size() Returns numrber of items in the queue
'''
class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def view(self):
        return self.items

q = Queue()
#print q.isEmpty()
q.enqueue(5)
q.enqueue("Vola")
q.enqueue(7)

print q.view()
print q.size()
q.dequeue()
print q.view()

print q.size()
q.dequeue()
q.dequeue()

print q.isEmpty()
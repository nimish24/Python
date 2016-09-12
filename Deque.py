__author__ = 'Nimish'
'''
    A DEQUE is a hybrid between a STACK and a QUEUE
    We can add and remove items from either ends of a Deque
    Deque(): creates new empty deque
    addFront(item)
    addRear(item)
    removeFront()
    removeRear()
    isEmpty()
    size()
'''

class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def view(self):
        return self.items

d = Deque()

d.addFront('hello')
d.addRear('world')
print d.size()
print d.view()
d.addFront(6)
d.addRear(9)
print d.view()
d.removeFront()
d.removeRear()
print d.view()
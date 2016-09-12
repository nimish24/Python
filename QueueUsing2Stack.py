class queue2stacks():
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                return self.outstack.append(self.instack.pop())

        return self.outstack.pop()

    def view(self):
        return self.instack

q = queue2stacks()

q.enqueue(5)
q.enqueue(4)
q.enqueue(2)
q.enqueue(1)
q.enqueue(0)

print q.view()
print q.dequeue()

print q.dequeue()
q.dequeue()





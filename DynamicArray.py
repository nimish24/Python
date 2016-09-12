__author__ = 'Nimish'
import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0 #count of elements
        self.capacity = 1 #1 to accept only 1 element by default
        self.A = self.make_array(self.capacity)

    def __len__(self): #return no of elements stored in the array
        return  self.n

    def __getitem__(self, k): #return element at index k
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        return self.A[k]

    def append(self,elem): #adds element
        if self.n == self.capacity:
            self._resize(2*self.capacity) #2x if capacity isn't enough
        self.A[self.n] = elem
        self.n +=1

    def _resize(self,new_capacity): #resize the internal array to the capacity of new_capacity
        B = self.make_array(new_capacity)

        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self,new_capacity):

        return (new_capacity * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
print len(arr)
arr.append(2)
print len(arr)
arr[0]
arr[1]
print arr.__getitem__(1)

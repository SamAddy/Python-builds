"""
Task

The List method addAll(i,c) inserts all elements of the Collection, c, into the list at position i. (The add(i, x)
method is a special case where c = {x}.) It is not efficient to implement addAll(i,c) by repeated calls to add(i,x).
Design and implement a more efficient implementation in which there is no repeated calls to the add(i,x) method.

Samle input

The sample input will be as follows:

list: 1 2 3
list2: 4 5 6

Expected output

The expected output will be as follows:

List elements:
1
4
5
6
2
3
"""

from utils import new_array
from base import BaseList

class ArrayList(BaseList):
    def __init__(self, t):
        self.a = []
        self.n = 0
    # Function to resize the array
    def resize(self):
        b = [None] * max(self.n * 2, 1)
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b
    # Function to get values
    def get(self, i):
        if i < 0 or i > self.n - 1:
            raise IndexError("Index out of bounds")
        return self.a[i]
    # Function to get size
    def size(self):
        return self.n
    # Function to add values
    def add(self, i, x):
        if i < 0 or i > self.n:
            raise IndexError("Index out of bounds")
        if self.n + 1 > len(self.a):
            self.resize()
        self.a.insert(i, x)
        self.n += 1
    # Function ot add all values
    def addAll1(self, idx, collection):
        for element in collection:
            self.add(idx, element)
            idx += 1
    # Resize helper function
    def resize2(self, newn):
        b = [None] * max(newn, 1)
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b
    # New addAll function
    def addAll2(self, idx, collection):
        # Write code here
        if idx < 0 or idx > self.n:
            raise IndexError("Index out of bounds")
        # Resize the list
        if self.n + len(collection) > len(self.a):
            self.resize()
        # Insert each element in collection into the list
        for element in collection:
            self.a.insert(idx, element)
            idx += 1
        self.n += len(collection)

if __name__ == "__main__":
    # Creating object
    list1 = ArrayList(int)
    # Adding values
    list1.add(0, 1)
    list1.add(1, 2)
    list1.add(2, 3)
    # Creating seconf object
    list2 = ArrayList(int)
    # Adding values
    list2.add(0, 4)
    list2.add(1, 5)
    list2.add(2, 6)
    # Adding list
    list1.addAll2(1, list2)
    # Updated list
    print("List elements:")
    for i in range(list1.size()):
        print(list1.get(i))
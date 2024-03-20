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


solution explanation:
Solution

The reason why implementing addAll(i, c) by repeated calls to add(i, x) is not efficient is the following:

If we consider an ArrayList as the underlying data structure, the add(i, x) operation has a time complexity of O(n)O(n)
because it requires shifting all the elements after the insertion point to make room for the new element. It also checks
and calls the resize() operation that adds one more memory cell and copies the whole existing array on each call to
add(i,x). Therefore, if we use add(i, x) in a loop to add each element from the collection c, the time complexity would
be O(n2)O(n2), as we would have to shift elements and copy the whole array multiple times for each insertion.

To design a more efficient implementation for addAll(i, c), we can add the efficiency in the following way: adding all
needed cells in a single call to the modified resize() and allowing efficient insertion by inserting multiple elements
at a specific position shifting all affected elements only once.

We have implemented the conventional addAll() as addAll1() and the efficient version as addAll2(). We have also
implemented the efficient resize2() method to replace the conventional resize() to avoid multiple calls of the same.
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
        if idx < 0 or idx > self.n:
            raise IndexError("Index out of bounds")
        collectionSize = len(collection)
        if self.n + collectionSize > len(self.a):
            self.resize2(self.n + collectionSize)

        for i in range(self.n - idx):
            self.a[idx + collectionSize + i] = self.a[idx + i]

        currentIndex = idx
        for element in collection:
            self.a[currentIndex] = element
            currentIndex += 1
        self.n += collectionSize

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
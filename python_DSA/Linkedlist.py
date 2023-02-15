
class _Node:
    __slots__ = '_elements', '_next'

    def __init__(self, element, next):
        self._elements = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addany(self, e, position):
        newest = _Node(e, None)
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size += 1



    def addfirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def deletefirst(self):
        if self.isempty():
            print('l list is empty ')
            return
        p = self._head
        self._head = p._next
        self._size -=1
        if self.isempty():
            self._tail = None
        return p._elements

    def delete_any(self,position):
        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        e = p._next
        p._next =e._next
        self._size -= 1
        return e._elements




    def delete_last(self):
        if self.isempty():
            print('list is empty')
            return
        p = self._head
        i = 1
        while i<self._size - 1:
            p = p._next
            i+=1
        e = p._next
        p._next = None
        self._size -= 1
        return e._elements


    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._elements == key:
                return index
            p = p._next
            index += 1
        return -1

    def display(self):
        p = self._head
        while p :
            print(p._elements,end='-->')
            p = p._next
        print()

    def reversing(self):
        p = self._head
        prev = None
        while p:
            temp = p._next
            p._next = prev
            prev = p
            p = temp
        self._head = prev
        return prev








l = LinkedList()
l.addlast(7)
l.addlast(2)
l.addlast(78)
l.addlast(8)
l.addfirst(5)
l.display()
print('size of l:',len(l))
# print("index of numb:",l.search(0))
l.addfirst(3 )
l.addlast(9)
l.display()
print('size of l:',len(l))

l.addany(9,2)
l.display()

print('deleted element', l.deletefirst())
l.display()

print('size of l:',len(l))

print('deleted element', l.delete_last())


l.display()
print('size of l:',len(l))

print('deleted element', l.delete_any(2))
l.display()
print('size of l:',len(l))
print("---------")
print(l.reversing())
l.display()
# l.addfirst(5)
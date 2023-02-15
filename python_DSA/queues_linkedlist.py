
'''class for node'''

class _Node():
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next

''' for linked linsted list '''

class QueuesLinkedList():

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1


    def dequeue(self):

        if self.isempty():
            print("queue is empty")
            return
        e = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e

    def first(self):
        if self.isempty():
            print("Queue is emppty")
            return
        return self._front._element

    def display(self):

        p = self._front
        while p:
            print(p._element,end="-->")
            p = p._next
        print()

q = QueuesLinkedList()
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
print(q.first())
print(q.isempty(),',  *length:',len(q))


q.display()


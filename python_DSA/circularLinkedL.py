class _Node():
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class circularLinkedList():

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def insertFirst(self, e):
        p = _Node(e, None)
        if self.isempty():
            self._head = p
            self._tail = p

        else:

            p._next = self._head
            self._head = p
            self._tail._next = self._head


        self._size += 1


    def insertlast(self, e):
        newNode = _Node(e, None)
        if self.isempty():
            self._head = newNode
            self._tail = newNode

        else:
            self._tail._next = newNode
            self._tail = newNode
            self._tail._next = self._head
        self._size += 1

    def deletefirst(self):
        if self.isempty():
            print("list is empty")
        else:
            self._head = self._head._next
            self._tail._next = self._head
            self._size -= 1

    def deletelast(self):
        if self.isempty():
            print("list is empty")
        else:
            p = self._head
            while True:
                if p._next._next == self._head:
                    p._next = self._head
                    self._tail = p
                    break
                p = p._next

    def display(self):
        p = self._head
        while True:
            print(p._element, end="-->")
            if p._next is self._head:
                break
            p = p._next

    def head(self):
        print(self._head._element)

    def tail(self):
        print(self._tail._element, )

    def isCircularLinkedList(self):
        return self._head == self._tail._next

    def search(self, e):
        p = self._head
        while True:
            if p._element == e:
                print(p._element)
                break
            if p._next == self._head:
                break
            p = p._next


cl = circularLinkedList()
cl.insertlast(35)
cl.insertFirst(10)
cl.insertlast(70)
cl.insertFirst(90)
cl.insertFirst(101)
cl.insertlast(21)
cl.insertFirst(40)
cl.display()
cl.deletefirst()
print()
cl.display()
cl.deletelast()
print()
cl.display()
print()
cl.head()
cl.tail()
print("is this completly circular", cl.isCircularLinkedList())
cl.search(35)

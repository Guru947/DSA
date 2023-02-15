class Node:
    def __init__(self, previous, element, next):
        self._previous = previous
        self._element = element
        self._next = next


class doublelinkedlist:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def addfirst(self, e):
        new = Node(None, e, None)
        if self._head == None:
            self._head = new
            self._tail = new
            self._length += 1
            return
        new._next = self._head
        self._head._previous = new
        self._head = new
        self._length += 1

    def addlast(self, e):
        new = Node(None, e, None)
        if self._head == None:
            self._head = new
            self._tail = new
            self._length += 1
            return
        self._tail._next = new
        new._previous = self._tail
        self._tail = new
        self._length += 1

    def addany(self, e, position):
        new = Node(None, e, None)
        if self._head == None:
            self._head = new
            self._tail = new
            self._length += 1
            return

        p = self._head
        i = 1
        while i < position - 1:
            p = p._next
            i += 1
        new._next = p._next
        new._previous = p
        p._next = new
        self._length += 1

    def deletefirst(self):
        if self._head == None:
            print("double limked list is empty")
        else:
            self._head._next._previous = None
            self._head = self._head._next
            self._length -= 1

    def deletelast(self):
        if self._head == None:
            print("double limked list is empty")
        else:
            self._tail._previous._next = None
            self._tail = self._tail._previous
            self._length -= 1

    def deleteany(self, position):
        if self._head == None:
            print("double limked list is empty")
        else:
            p = self._head
            i = 1
            while i < position - 1:
                p._next._next._previos = p
                p._next = p._next._next

                p = p._next
                i +=1
        self._length -= 1

    def search(self,e):
        p = self._head
        while p:
            if p._element == e:
                return "element found value is",p._element
            p = p._next
        return "element not found"


    def display(self):
        p = self._head
        while p:
            print(p._element, end="<-->")
            p = p._next

    def displayFullInfo(self):
        p = self._head
        while p:
            print(p._previous, p._element, p._next, end="<-->")
            p = p._next


dl = doublelinkedlist()
dl.addfirst(34)
dl.addfirst(33)
dl.addfirst(32)
dl.addfirst(31)
dl.addlast(35)
dl.addlast(36)
dl.addany(32.5, 3)
dl.display()
print()
dl.deletefirst()
dl.deletelast()
dl.deleteany(3)
dl.display()
print()
print(dl._length)
print(dl.search(0))
print()
# dl.displayFullInfo()

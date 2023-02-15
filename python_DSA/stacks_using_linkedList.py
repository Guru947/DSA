class _Node():
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class stacks():

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, element):
        newest = _Node(element, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.isempty():
            print('stack is empty')
            return

        e = self._top._element
        self._top = self._top._next
        self._size -= 1
        return e

    def top(self):
        if self.isempty():
            print('stack is mt')
            return
        return self._top._element

    def display(self):

        if self.isempty():
            return
        else:
            p = self._top
            while p:
                print(p._element, end="-->")
                p = p._next
            print()


s = stacks()
s.push(1)
s.push(2)
s.push(3)

s.display()
print(s.isempty())
s.pop()
print(s.top())
s.display()

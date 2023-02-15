'''
        stacks = stacks is a collection od objects
    LIFO(last in first out) first inserted value is deleted
    FIFO(first in last out) first in first value is deteted
'''


class stackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print('stack is empty')
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print('stack is empty')
            return
        return self._data[-1]


sl = stackArray()
sl.push(1)
sl.push(2)
sl.push(3)
sl.push(4)
print(sl._data)
print('poped element', sl.pop())
print('top lement', sl.top())
print('poped element', sl.pop())

print(sl._data)
print('length is:', len(sl))

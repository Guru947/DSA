class Node:
    __slots__ = '_left', '_element', '_right'

    def __init__(self, element, left=None, right=None):
        self._left = left
        self._element = element
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, e, left, right):
        self._root = Node(e, left._root, right._root)

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=' ')
            self.inorder(troot._right)

    def preorder(self, troot):
        if troot:
            print(troot._element, end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

    def levelorder(self):
        Q = Queue()
        t = _root
        print()



x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
x.maketree(40, a, a)
y.maketree(60, a, a)
z.maketree(20, x, a)
r.maketree(50, a, y)
s.maketree(30, r, a)
t.maketree(10, z, s)
print("inorder")
t.inorder(t._root)
print("\npostorder")
t.postorder(t._root)
print("\npreoder")
t.preorder(t._root)

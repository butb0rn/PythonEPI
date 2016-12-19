class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        self.parent = None

def lcd(n0, n1):
    hashSet = set()
    while n0 or n1:
        if n0:
            if n0 in hashSet:
                return n0
            else:
                hashSet.add(n0)
            n0 = n0.parent

        if n1:
            if n1 in hashSet:
                return n1
            else:
                hashSet.add(n1)
            n1 = n1.parent

root = Node("a")
root.left = Node("b")
root.left.parent = root
root.left.right = Node("e")
root.left.right.parent = root.left
root.right = Node("f")
root.right.parent = root
root.left.left = Node("c")
root.left.left.parent = root.left

print lcd(root.left.left, root.left.right).val

class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findNextKey(root, key):
    if not root: return
    if key > root.data:
        return findNextKey(root.right, key)
    if key < root.data:
        p = findNextKey(root.left, key)
        if not p: return root.data
        return p
    if key == root.data and root.right:
        return root.right.data

    return

tree = Node(8, Node(5, Node(3), Node(7)), Node(12, Node(9, None, Node(11, Node(10))), Node(14)))

print findNextKey(tree, 9)

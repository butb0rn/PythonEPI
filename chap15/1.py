class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isBST(tree):
    return bstHelper(tree, None, None)

def bstHelper(root, minNode, maxNode):
    if not root: return True
    if maxNode:
        if root.data > maxNode: return False
    if minNode:
        if root.data < minNode: return False

    return bstHelper(root.left, minNode, root.data) and bstHelper(root.right, root.data, maxNode)




tree = Node(8, Node(5, Node(3), Node(7)), Node(12, Node(9), Node(14)))
print isBST(tree)

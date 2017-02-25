class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findLCA(bst, n1, n2):
    if not bst: return None

    if bst.data > n1.data and bst.data > n2.data: return findLCA(bst.left, n1, n2)
    if bst.data < n1.data and bst.data < n2.data: return findLCA(bst.right, n1, n2)

    return bst



tree = BST(8, BST(5, BST(3), BST(7)), BST(12, BST(9), BST(14)))

print findLCA(tree, tree.left.left, tree.right.right).data

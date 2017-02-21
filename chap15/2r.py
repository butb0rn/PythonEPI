class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def findFirstGreaterKey(tree, k):
    if not tree: return None

    while tree:
        if k < tree.data:
            node = tree
            tree = tree.left
        else:
            tree = tree.right

    return node


tree = Tree(8, Tree(5, Tree(3), Tree(7)), Tree(12, Tree(9, None, Tree(11, Tree(10))), Tree(14)))

print findFirstGreaterKey(tree, 10).data

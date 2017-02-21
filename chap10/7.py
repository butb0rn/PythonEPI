class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorderTraversal(tree):
    if not tree: return None
    s = []

    while tree or s:
        if tree:
            s.append(tree)
            tree = tree.left
        else:
            tree = s.pop()
            print tree.data,
            tree = tree.right


tree = Tree(8, Tree(5, Tree(3), Tree(7)), Tree(12, Tree(9, None, Tree(11, Tree(10))), Tree(14)))
inorderTraversal(tree)

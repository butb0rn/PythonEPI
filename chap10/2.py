class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child


def isSymmetric(tree):
    return tree and symmetricHelper(tree.left, tree.right)


def symmetricHelper(t1, t2):
    if not t1 and not t2: return True

    if t1 and t2:
        return t1.data == t2.data and \
                symmetricHelper(t1.left, t2.right) and \
                symmetricHelper(t1.right, t2.left)

    return False


test_tree = Tree(10, Tree(8, Tree(5), Tree(6)), Tree(8, Tree(6), Tree(5)))
print isSymmetric(test_tree)

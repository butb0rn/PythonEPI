def sym_checker(tree):
    print is_sym(tree.left, tree.right)


def is_sym(left, right):
    if left == None and right == None: return True
    elif left != None and right != None: return left.data == right.data and is_sym(left.left, right.right) \
                      and is_sym(left.right, right.left)
    return False

class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child


test_tree = Tree(10, Tree(2), Tree(2)) #true
# test_tree = Tree(10, Tree(2, Tree(6, Tree(8, Tree(16)))), Tree(4))
sym_checker(test_tree)

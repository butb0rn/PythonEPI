class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child


def balanced_status(input_tree):
    print is_balanced(input_tree) != -1

def is_balanced(tree):
    if tree == None: return 0

    left_side = is_balanced(tree.left)
    if left_side == -1: return -1

    right_side = is_balanced(tree.right)
    if right_side == -1: return -1

    if abs(left_side - right_side) > 1: return -1

    return max(left_side, right_side) + 1


#test_tree_one = Tree(10, Tree(2), Tree(4)) #true
test_tree_two = Tree(10, Tree(2, Tree(6, Tree(8, Tree(16)))), Tree(4))
balanced_status(test_tree_two)

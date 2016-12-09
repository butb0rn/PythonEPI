class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child


def get_sum_tree(tree):
    print calculate_sum_tree(tree, 0)


def calculate_sum_tree(tree, partialSum):

    if tree == None:
        return 0

    partialSum = tree.data + partialSum * 2
    if tree.left == None and tree.right == None:
        return partialSum

    return calculate_sum_tree(tree.left, partialSum) + calculate_sum_tree(tree.right, partialSum)


t1 = Tree(1)
t2 = Tree(1)
t3 = Tree(0)
t4 = Tree(1)
t5 = Tree(0)
t6 = Tree(1)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t5.left = t6


get_sum_tree(t1)

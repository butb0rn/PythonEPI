class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child

def find_node(tree, target):
    print get_node_specified_sum(tree, target, 0)


def get_node_specified_sum(tree, target, partialSum):
    if tree == None: return None

    partialSum += tree.data
    if tree.left == None and tree.right == None:
        return partialSum == target

    return get_node_specified_sum(tree.right, target, partialSum) or get_node_specified_sum(tree.left, target, partialSum)

#test
t1 = Tree(5)
t2 = Tree(3)
t3 = Tree(2)
t4 = Tree(7)
t5 = Tree(9)
t6 = Tree(6)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t5.left = t6


find_node(t1, 23)

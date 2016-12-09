class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child
        self.elements = 0

def find_lca(tree,n1,n2):
    result = get_lca_tree(tree, n1, n2)
    if result.elements == 2:
        return result
    else:
        None

def get_lca_tree(tree, n1, n2):
    if tree == None:
        return Tree()
    elements = 0
    left_side = get_lca_tree(tree.left, n1, n2)
    if left_side.elements == 2: return tree.left

    right_side = get_lca_tree(tree.right, n1, n2)
    if right_side.elements == 2: return tree.right

    if tree == n1:
        elements += 1
    if tree == n2:
        elements += 1

    tree.elements = left_side.elements + right_side.elements + elements

    return tree

t1 = Tree(1)
t2 = Tree(2)
t3 = Tree(3)
t4 = Tree(4)
t5 = Tree(5)
t6 = Tree(6)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5
t5.left = t6
print get_lca_tree(t1, t3, t5).data

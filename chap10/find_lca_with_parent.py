class Tree:
    def __init__(self, data=None, left_child=None, right_child=None, parent=None):
        self.data = data
        self.right = right_child
        self.left = left_child
        self.parent = parent

def find_lca(tree, n1, n2):
    if tree == None: return None

    n1_height = get_height(n1)
    n2_height = get_height(n2)

    if n1_height > n2_height:
        diff = abs(n1_height - n2_height)
        n1 = adjust_tree(n1, diff)

    else:
        diff = abs(n2_height - n1_height)
        n2 = adjust_tree(n2, diff)

    while n1 and n2 and n1 != n2:
        n1 = n1.parent
        n2 = n2.parent

    return n1


def get_height(n1):
    count = 0
    while n1:
        n1 = n1.parent
        count += 1
    return count

def adjust_tree(tree, diff):
    while diff > 0:
        tree = tree.parent
        diff -= 1
    return tree



t1 = Tree(1)
t2 = Tree(2)
t3 = Tree(3)
t4 = Tree(4)
t5 = Tree(5)
t6 = Tree(6)

t1.left = t2
t1.right = t3
t3.parent = t1
t2.parent = t1
t2.left = t4
t4.parent = t2
t2.right = t5
t5.parent = t2
t5.left = t6
t6.parent = t5

print find_lca(t1, t1, t6).data

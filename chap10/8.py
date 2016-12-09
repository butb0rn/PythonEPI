class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child

def get_preorder_travel(tree):
    stack = []

    while len(stack) > 0 or tree:
        if tree:
            print tree.data
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            tree = tree.right



t1 = Tree("a")
t2 = Tree("b")
t3 = Tree("c")
t4 = Tree("d")
t5 = Tree("e")

t1.left = t2
t1.right = t3
t2.right = t4
t4.left = t5


get_preorder_travel(t1)

class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.sibiling = None

def print_tree(tree, level):
    if tree == None: return
    print ' ' * level + str(tree.data)
    if tree.sibiling != None:
        print ' ' * level + " sib => " + str(tree.sibiling.data)
    else:
        print ' ' * level + " sib => " + "None"
    print_tree(tree.left, level + 1)
    print_tree(tree.right, level + 1)

def constructRightSibilings(tree):
    while tree and tree.left:
        populateRightSibilings(tree)
        tree = tree.left

def populateRightSibilings(tree):
    node = tree
    while node:
        node.left.sibiling = node.right
        if node.sibiling:
            node.right.sibiling = node.sibiling.left

        node = node.sibiling


tree = Tree("A", Tree("B"), Tree("C"))

constructRightSibilings(tree)
print_tree(tree,0)

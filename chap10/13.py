class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child

def print_tree(tree, level):
    if tree == None: return
    print ' ' * level + str(tree.data)
    print_tree(tree.left, level + 1)
    print_tree(tree.right, level + 1)


curr = 0
def getTree(arr):
    exp = [x.strip() for x in arr.strip().split(',')]
    return buildTree(exp)

def buildTree(preOrder):
    global curr
    root = preOrder[curr]
    curr += 1
    if root == "None":
        return None 
    return Node(root, buildTree(preOrder), buildTree(preOrder))


result = getTree("H, B, F, None, None, E, A, None, None, None, None")
print_tree(result,0)

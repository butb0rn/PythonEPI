class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child

def print_tree(tree, level):
    if tree == None: return
    print ' ' * level + str(tree.data)
    print_tree(tree.left, level + 1)
    print_tree(tree.right, level + 1)

cur = 0
def reconstructPreorderSubtree(preorder):
    global cur
    key = preorder[cur]
    cur += 1
    if not key: return None

    return Tree(key, reconstructPreorderSubtree(preorder), reconstructPreorderSubtree(preorder))


res = reconstructPreorderSubtree(["H", "B", "F", None, None, "E", "A", None, None, None, None])
print_tree(res, 0)

class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child

def createListOfLeaves(tree):
    result = []
    listHelper(tree, result)
    return result


def listHelper(tree, result):

    if not tree: return None
    if not tree.left and not tree.right:
        result.append(tree.data)
    else:
        listHelper(tree.left, result)
        listHelper(tree.right, result)

tree = Tree(314, Tree(6, Tree(271, Tree(28), Tree(0)), Tree(561, None, Tree(3, Tree(17)))), Tree(6, Tree(2),Tree(271)))
print createListOfLeaves(tree)

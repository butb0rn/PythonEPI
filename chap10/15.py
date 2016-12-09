class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child

def getExTree(tree):
    result = []
    if tree:
        result.append(tree.data)
        result.extend(leftSide(tree.left, True))
        result.extend(rightSide(tree.right, True))

    return result

def leftSide(tree, isBoundry):
    result = []
    if tree:
        if isLeaf or isBoundry:
            result.append(tree.data)

        result.extend(leftSide(tree.left, isBoundry))
        result.extend(leftSide(tree.right, isBoundry and tree.left == None))

    return result

def rightSide(tree, isBoundry):
    result = []
    if tree:
        result.extend(rightSide(tree.left, isBoundry and tree.right == None))
        result.extend(rightSide(tree.right, isBoundry))
        if isLeaf or isBoundry:
            result.append(tree.data)

    return result

def isLeaf(tree):
    if tree.left == None and tree.right == None:
        return True
    return False



tree = Tree("A", Tree("B", None, Tree("D",Tree("F"),None)), Tree("C", Tree("E", Tree("G"), Tree("H")), None))
print getExTree(tree)

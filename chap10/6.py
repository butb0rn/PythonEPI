class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child


def pathSumFinder(tree, partialSum, targetSum):
    if not tree: return False
    partialSum += tree.data

    if not tree.left and not tree.right:
        return partialSum == targetSum

    return pathSumFinder(tree.left, partialSum, targetSum) or \
           pathSumFinder(tree.right, partialSum, targetSum)

def hasPathSum(tree, targetSum):
    return pathSumFinder(tree, 0, targetSum)



tree = Tree(314, Tree(6, Tree(271, None, None), Tree(561, None, Tree(3))), None)


print hasPathSum(tree, 591)

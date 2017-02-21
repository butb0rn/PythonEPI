class Node(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = -1
        self.left = left
        self.right = right

def preorder(root):
    if root is not None:
        print root.data,
        preorder(root.left)
        preorder(root.right)

def generateAllBinaryTrees(n):
    result = []
    if n == 0:
        result.append(None)

    for numLeftNodes in range(n):
        numRightNodes = n - 1 - numLeftNodes
        leftSubTrees = generateAllBinaryTrees(numLeftNodes)
        rightSubTrees = generateAllBinaryTrees(numRightNodes)
        for left in leftSubTrees:
            for right in rightSubTrees:
                result.append(Node(left, right))
    return result

res = generateAllBinaryTrees(2)
print "*******"
for r in res:
    print preorder(r)

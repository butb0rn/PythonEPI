class Tree:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def constructFromPreorder(preorder, inorder):
    dic = {}
    for i in range(len(inorder)):
        dic[inorder[i]] = i

    return treeHelper(preorder, 0, len(preorder), 0, len(inorder), dic)


def treeHelper(preorder, preStart, preEnd, inStart, inEnd, mapInorderIdx):
    if preEnd <= preStart or inEnd <= inStart: return None

    rootIdx = mapInorderIdx[preorder[preStart]]
    leftSideSize = rootIdx - inStart
    print preorder[preStart],
    return Tree(preorder[preStart], \
                treeHelper(preorder, preStart+1, preStart+leftSideSize+1, inStart, rootIdx, mapInorderIdx), \
                treeHelper(preorder, preStart+leftSideSize+1, preEnd, rootIdx+1, inEnd, mapInorderIdx)
                )

constructFromPreorder("HBFEACDGI","FBAEHCDIG")

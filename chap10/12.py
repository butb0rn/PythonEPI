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



def getTree(preOrder, inOrder):
    dic = {}
    for idx in range(len(inOrder)):
        dic[inOrder[idx]] = idx

    return buildTree(preOrder, 0, len(preOrder), 0, len(inOrder), dic)


def buildTree(preOrder, startPre, finishPre, startIn, finishIn, dic):
    if finishPre <= startPre or finishIn <= startIn:
        return None

    rootIdx = dic[preOrder[startPre]]
    leftSideSize = rootIdx - startIn

    return Node(preOrder[startPre], \
           buildTree(preOrder, startPre+1, startPre+leftSideSize+1, startIn, rootIdx, dic), \
           buildTree(preOrder, startPre+1+leftSideSize, finishPre, rootIdx+1, finishIn, dic))

x = getTree("HBFEACDGI","FBAEHCDIG")
print_tree(x, 0)

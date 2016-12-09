class Tree:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child
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


def getTree(tree):
    if tree:
        getSibiling(tree, 0)

dic = {}
def getSibiling(tree, level):
    global dic
    if tree:
        if level in dic.keys():
            temp = dic[level]
            temp.sibiling = tree
            dic[level] = tree
        else:
            dic[level] = tree

        getSibiling(tree.left, level + 1)
        getSibiling(tree.right, level + 1)


tree = Tree("A", Tree("B", None, Tree("D",Tree("F"),None)), Tree("C", Tree("E", Tree("G"), Tree("H")), None))
#tree = Tree("A", Tree("B", Tree("D"), Tree("E")), Tree("C", Tree("F"), Tree("G")))
getTree(tree)
print_tree(tree,0)

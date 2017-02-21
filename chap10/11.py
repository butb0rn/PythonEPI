class Tree(object):
    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

def inorderTraversal(tree):
    cur = tree
    prev = None
    result = []

    while cur:

        if cur.parent == prev:
            if cur.left:
                nexti = cur.left
            else:
                if cur.right:
                    nexti = cur.right
                else:
                    nexti = cur.parent
                result.append(cur)

        elif cur.left == prev:
            if cur.right:
                nexti = cur.right
            else:
                nexti = cur.parent
            result.append(cur)

        else:
            nexti = cur.parent

        prev = cur
        cur = nexti

    return result

tree = Tree(10)
t1 = Tree(5, None, None, tree)
t2 = Tree(8, None, None, t1)
t3 = Tree(7, None, None, t2)
tree.left = t1
t1.right = t2
t2.left = t3

t4 = Tree(14, None, None, tree)
t5 = Tree(12, None, None, t4)
tree.right = t4
t4.left = t5

print [x.data for x in inorderTraversal(tree)]

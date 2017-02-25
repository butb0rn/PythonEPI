class Tree(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Interval(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

def rangeLookupInBST(tree, interval):
    result = []
    rangeLookupHelper(tree, interval, result)
    return result


def rangeLookupHelper(tree, interval, result):
    if not tree: return

    if tree.data >= interval.left and tree.data <= interval.right:
        rangeLookupHelper(tree.left, interval, result)
        result.append(tree.data)
        rangeLookupHelper(tree.right, interval, result)

    elif tree.data < interval.left:
        rangeLookupHelper(tree.right, interval, result)

    else:
        rangeLookupHelper(tree.left, interval, result)


tree = Tree(15, Tree(9, Tree(7), Tree(11)), Tree(19, Tree(17), Tree(45)))
interval = Interval(10, 42)
print rangeLookupInBST(tree, interval)

class BST(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def print_tree(tree):
    if tree == None: return
    print_tree(tree.left)
    print tree.data,
    print_tree(tree.right)

def rebuildBSTFromPreorder(preorderSeq):
    return preorderHelper(preorderSeq, 0, len(preorderSeq))

def preorderHelper(seq, start, end):
    if end <= start: return None
    tp = start + 1

    while tp < end and seq[tp] < seq[start]:
        tp += 1

    return BST(seq[start], preorderHelper(seq, start+1, tp), preorderHelper(seq, tp, end))


seq = [43, 23, 37, 29, 31, 41, 47, 53]
print_tree(rebuildBSTFromPreorder(seq))

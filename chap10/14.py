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


def getLinkList(tree):
    stack = []
    result = []
    buildLinkList(tree, stack, result)
    return result


def buildLinkList(tree, stack, result):
    if tree:
        stack.append(tree)
        buildLinkList(tree.left, stack, result)
    else:
        if stack:
            tree = stack.pop()
            if tree.left == None and tree.right == None:
                result.append(tree)
            buildLinkList(tree.right, stack, result)
        else:
            return

x = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(6)))
for node in getLinkList(x):
    print node.data

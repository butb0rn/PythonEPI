class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.val = data
        self.right = right_child
        self.left = left_child

def binaryTreePaths(root):
        partial = []
        paths = []
        result = []
        findPaths(root, partial, paths)
        result.append(["->".join(str(node.val) for path in paths for node in path)])
        return result

def findPaths(root, partial, paths):
    if root == None:
        return
    partial.append(root)
    if root.left == None and root.right == None:
        paths.append([i for i in partial])
        partial.pop()
        return

    findPaths(root.left, partial, paths)
    findPaths(root.right, partial, paths)
    partial.pop()



x = Node(1, Node(2, None, Node(5)), Node(3))
print binaryTreePaths(x)

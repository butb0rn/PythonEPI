class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.val = data
        self.right = right_child
        self.left = left_child

class Solution(object):
    def pathHelper(self, root, partial, result):
        if not root: return
        partial.append(root.val)
        if not root.left and not root.right:
            result.append(partial[:])
            return
        if root.left:
            self.pathHelper(root.left, partial, result)
            partial.pop()
        if root.right:
            self.pathHelper(root.right, partial, result)
            partial.pop()


    def binaryTreePaths(self, root):
        result = []
        self.pathHelper(root, [], result)
        return ["->".join(map(str, p)) for p in result]

x = Node(1, Node(2, None, Node(5)), Node(3))
print rootToLeafPath(x)

# def rootToLeafPath(root):
#     if not root: return []
#     result = [str(root.val)+'->'+path for path in rootToLeafPath(root.left)]
#     result += [str(root.val)+'->'+path for path in rootToLeafPath(root.right)]
#     return result or [str(root.val)]

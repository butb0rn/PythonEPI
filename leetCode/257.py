class Node:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.val = data
        self.right = right_child
        self.left = left_child

def rootToLeafPath(root):
    if not root: return []
    result = [str(root.val)+'->'+path for path in rootToLeafPath(root.left)]
    result += [str(root.val)+'->'+path for path in rootToLeafPath(root.right)]
    return result or [str(root.val)]

x = Node(1, Node(2, None, Node(5)), Node(3))
print rootToLeafPath(x)

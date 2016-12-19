# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    class Node(object):
        def __init__(self, node, count=0):
            self.ancestor = node
            self.count = count

    def findLCA(self, root, p, q):
        x = self.lowestCommonAncestor(Node(root), p, q)
        return x.node

    def lowestCommonAncestor(self, root, p, q):
        if not root: return Solution().Node(None, 0)
        counter = 0
        left = self.lowestCommonAncestor(root.left, p, q)
        if left.count == 2: return left

        right = self.lowestCommonAncestor(root.right, p, q)
        if right.count == 2: return right

        if root.val == p.val or root.val == q.val: counter += 1
        counter += left.count + right.count

        if counter == 2: return Node(root, counter)

        return Solution().Node(None, counter)


root = TreeNode(0)
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(1)
r4 = TreeNode(4)
root.left = r1
root.right = r2
r1.right = r3
r1.left = r4
x=Solution().lowestCommonAncestor(root,r1,r4)
print x.ancestor

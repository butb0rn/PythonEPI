'''
Binary Tree Longest Consecutive Sequence
For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(self, root, key, res):
            if not root: return 0
            if root.val == key:
                key += 1
                res += 1
            else:
                key = root.val + 1
                res = 1
            left = helper(self, root.left, key, res)
            right = helper(self, root.right, key, res)
            return max(left, right, res)


        if not root: return 0
        key = root.val
        return helper(self,root, root.val, 0)

'''
Given a non-empty binary search tree and a target value,
find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):

        def helper(root, target):
            if not root: return (sys.maxint,sys.maxint)
            val = abs(root.val - target)
            c = helper(root.left, target) if target < root.val else helper(root.right, target)
            return min(c, (val, root.val))

        return helper(root, target)[1]

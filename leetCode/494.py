class Solution(object):
    def findTargetSumWays(self, nums, S):
        cache = {}
        def helper(idx, s):
            if (idx, s) not in cache:
                r = 0
                if idx == len(nums):
                    if s == 0: r = 1
                else:
                    r = helper(idx+1, s+nums[idx]) + helper(idx+1, s-nums[idx])
                cache[(idx,s)] = r

            return cache[(idx, s)]

        return helper(0, S)

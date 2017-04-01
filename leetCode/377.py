'''
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
'''

class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [1] + [0] * target
        for i in range(1, len(dp)):
            dp[i] = sum(dp[i-n] for n in nums if i-n >= 0)

        return dp[target]

'''
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''

def findMaxConsecutiveOnes(nums):
        startIdx = 0
        cutIdx = -1
        maxOnes = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                maxOnes = max(maxOnes, i-startIdx)
                startIdx = cutIdx+1
                cutIdx = i

        return max(maxOnes, len(nums)-startIdx)

s = [1,1,0,1]
print findMaxConsecutiveOnes(s)

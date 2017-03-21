'''
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
'''

def summaryRanges(nums):
    res = []
    for i in range(len(nums)):
        if res and nums[i] - res[-1][-1] == 1:
            x = res.pop()
            res.append([x[0], nums[i]])
        else:
            res.append([nums[i]])

    return ['->'.join(map(str,r)) for r in res]


print summaryRanges([0,1,2,4,5,7,9,10,11,14])

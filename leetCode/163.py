'''
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''

def findMissingRanges(nums, lower, upper):
    nums.insert(0,lower-1)
        nums.append(upper+1)
        out = []
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 2:
                out.append([nums[i-1]+1])
            elif nums[i] - nums[i-1] > 2:
                out.append([nums[i-1]+1, nums[i]-1])

        return ["->".join(map(str,x)) for x in out]

nums = [0, 1, 3, 50, 75]
print findMissingRanges([1, 3, 50, 75], 0, 99)

import sys
def findMaxSubarray(nums, key):

    sumi = 0
    maxLen = -sys.maxint - 1
    dic = {}
    for idx in range(len(nums)):
        sumi += nums[idx]
        if sumi == key:
            maxLen = max(maxLen, idx+1)
        diff = sumi - key
        if diff in dic.keys():
            subLen = idx - dic[diff]
            maxLen = max(maxLen, subLen)

        if sumi not in dic.keys():
            dic[sumi] = idx

    if (maxLen == -999):
        return 0
    else:
        return maxLen



# l1 = [-2, -1, 2, 1]
l1 = [1, -1, 5, -2, 3]
print findMaxSubarray(l1, 3)



# result = []
# startIdx = 0
# total = 0
# for idx in range(len(nums)):
#     for i in range(idx+1, len(nums)):
#         total += nums[i]
#         if total == key:
#             result.append(i-startIdx)
#             startIdx = i+1
# return result

def generatePermutations(nums):
    if len(nums) < 1: return [""]
    result = []
    tmp = []
    for i in range(len(nums)):
        tmp = generatePermutations(nums[:i]+nums[i+1:])
        [result.append(str(nums[i])+subList) for subList in tmp]
    return result


res = generatePermutations([1,2,3])
print [map(int, x) for x in res]

def threeSum(nums):
    dic = {}
    result = set()
    for i in range(len(nums)-1):
        a = nums[i]
        for j in range(i+1, len(nums)):
            b = nums[j]
            c = (a+b)*-1
            if c in dic.keys():
                tup = tuple(sorted((a,b,c)))
                if tup not in result:
                    result.add(tup)
        dic[a] = i
    return [list(i) for i in result]
s = [-1, 0, 1, 2, -1, -4]
print threeSum(s)

def test(nums):
    nums.sort()
    res = []
    print nums
    for i in range(len(nums)-1):
        idx = len(nums)-1
        j = i+1
        while j < len(nums) and idx > j:
            if nums[j]+nums[idx]+nums[i] == 0:
                res.append([nums[j],nums[idx],nums[i]])
                j+= 1
            elif nums[j]+nums[idx]+nums[i] > 0 :
                idx -= 1
            else:
                j += 1

    return list(set(map(tuple, res)))


print test([-1, 0, 1, 2, -1, -4])

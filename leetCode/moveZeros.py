def moveZeros(nums):
    idx = 0
    while idx < len(nums):
        if nums[idx] == 0:
            nextIdx = idx
            while nextIdx < len(nums)-1 and nums[nextIdx] == 0:
                nextIdx += 1
                
            nums[idx], nums[nextIdx] = nums[nextIdx], nums[idx]
        idx += 1
    return nums

print moveZeros([0,1,0,3,12])

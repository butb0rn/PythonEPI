def removeDuplicatess(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i, nums[:i]

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 2: return nums[:2]
    dup = nums[0]
    cur, idx = 0, 1

    while idx < len(nums):
        extra = 0
        while idx < len(nums)-1 and nums[idx] == dup:
            extra = 1
            idx += 1

        if extra: nums[cur+1] = dup
        dup = nums[idx]
        nums[cur+1+extra], nums[idx] = nums[idx],nums[cur+1+extra]
        cur += 1 + extra
        idx += 1

    if nums[cur] == nums[cur-1]:
        extra =0
    return nums[:cur+extra]

print removeDuplicates([1,1])

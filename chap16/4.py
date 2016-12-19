def generateSubs(nums):
    def isActive(bit, l):
        return (l >> bit) & 1


    subsets = []
    for i in range(2**len(nums)):
        sub = []
        for bit in range(len(nums)):
            if isActive(bit, i):
                sub.append(nums[bit])

        subsets.append(sub)
    return subsets


print generateSubs([1,2,3])

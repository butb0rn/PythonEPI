def hasThreeSum(l, k):
    for e in sorted(l):
        goal, i, j= k-e, 0, len(l)-1
        while i <= j:
            partialRes = l[i]+l[j]
            if partialRes == goal: return True
            elif partialRes < goal: i += 1
            else: j -= 1

    return False


print hasThreeSum([11,2,5,7,3], 9)

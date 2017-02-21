def searchEntryEqualToIndex(l):
    left = 0
    right = len(l)-1

    while left <= right:
        mid = left + right-left/2
        diff = l[mid] - mid
        if diff == 0:
            return mid
        if diff > 0:
            right = mid-1
        else:
            left = mid+1

    return -1


print searchEntryEqualToIndex([-2,0,2,4,6,7,9])

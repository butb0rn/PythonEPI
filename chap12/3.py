def getSmallest(arr):
    if not arr: return
    idx = findSmallest(arr, 0, len(arr)-1)
    return idx,arr[idx]


def findSmallest(arr, left, right):
    if right == left: return left
    mid = left + (right-left)/2
    if arr[mid] > arr[right]:
        return findSmallest(arr, mid+1, right)
    elif arr[mid] < arr[right]:
        return findSmallest(arr, left, mid)
    else:
        left = findSmallest(arr, left, mid)
        right = findSmallest(arr, mid+1, right)
        return min(left, right)



s = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
res = getSmallest(s)
print "index:" + str(res[0]) + " -> " + str(res[1])

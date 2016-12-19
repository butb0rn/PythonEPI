def findPivot(l, left, right):
    if not l: return
    p = l[right]
    idx = left
    for i in range(left, right):
        if l[i] > p:
            l[idx], l[i] = l[i], l[idx]
            idx+=1

    l[idx], l[right] = l[right], l[idx]
    return idx


def findKth(l, k):
    left = 0
    right = len(l)-1
    while left <= right:
        pivot = findPivot(l, left, right)
        if pivot == k-1:
            return l[pivot]
        elif pivot > k-1:
            right = pivot - 1
        else:
            left = pivot + 1

#12 11 10 9 8 7 6 5 4 3 2 1
print findKth([3,9,2,8,7,5,4,10,11,12,6,1], 10)

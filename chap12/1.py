def findFirstTime(l, key):
    if len(l) < 1:
        return
    print getIndexFirstTime(l, 0, len(l), key)


def  getIndexFirstTime(l, left, right, key):
    if right < left:
        return -1
    mid = left + (right-left)/2
    if l[mid] == key:
        if l[mid-1] == key:
            result = getIndexFirstTime(l, left, mid-1, key)
        else:
            result = mid
    elif l[mid] > key:
        result = getIndexFirstTime(l, left, mid-1, key)
    else:
        result = getIndexFirstTime(l, mid+1, right, key)

    return result

l = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
#108 -> 3
#285 -> 6
#111 -> -1
findFirstTime(l, 242)

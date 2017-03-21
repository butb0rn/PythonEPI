def sqRoot(num):
    left = 0
    right = num

    while left <= right:
        print left, right
        mid = left + (right-left)/2
        sq = mid * mid
        if sq <= num:
            left = mid + 1
        else:
            right = mid - 1

    return left-1


print sqRoot(26)

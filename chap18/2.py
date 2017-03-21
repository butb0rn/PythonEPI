def minWaitingList(l):
    l.sort()
    waitingTime, result = 0,0
    for i in range(len(l)-1):
        waitingTime += l[i]
        result += waitingTime

    return result


print minWaitingList([2,5,1,3])

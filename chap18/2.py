def minWaitingList(l):
    l.sort()
    waitingTime, result = 0,0
    for i in range(len(l)-1):
        waitingTime += l[i]
        result += waitingTime

    x = reduce(lambda x, y: x + y, l[:-1])
    return x


print minWaitingList([2,5,1,3])

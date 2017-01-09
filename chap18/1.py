def taskAsg(l):
    l.sort()
    s, e, res = 0, len(l)-1, []

    while s < e:
        res.append((l[s], l[e]))
        s += 1
        e -= 1

    return res

task = [5,2,1,6,4,4]
print taskAsg(task)

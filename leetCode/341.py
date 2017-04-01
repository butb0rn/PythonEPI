def flattenList(l):
    res = []
    for i in range(len(l)):
        if str(l[i]).isdigit():
            res.append(l[i])
        else:
            res += flattenList(l[i])

    return res

x = [[1,1],2,[1,1]]
print flattenList(x)

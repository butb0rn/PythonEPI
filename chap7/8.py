def findSeq(n):
    result = ['1']
    partialRes = []
    i = 0
    while i < n-1:
        exp = result[i]
        expLen = len(exp)
        idx = 0
        partialRes = []
        while idx < expLen:
            item = exp[idx]
            crr = 1

            while idx+1 < expLen and item == exp[idx+1]:
                idx += 1
                crr += 1

            partialRes += str(crr)+str(item)
            crr = 1
            idx += 1
        result += ["".join(partialRes)]
        i+=1

    return result

print findSeq(8)

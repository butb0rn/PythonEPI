def getSubsetsSizeK(n, k):
    def subsetHelper(n, k, partial, result, idx):
        if k == 0:
            result.append(partial[:])
            return
        for i in range(idx,n+1):
            partial.append(i)
            subsetHelper(n, k-1, partial, result, i+1)
            partial.pop()

    result = []
    subsetHelper(n, k, [], result, 1)
    return result


print getSubsetsSizeK(5, 2)

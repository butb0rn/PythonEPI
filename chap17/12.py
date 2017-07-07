def longestNonDecSubseq(l):
    maxLen = [1 for i in range(len(l))]
    for i in range(1, len(l)):
        for j in range(i):
            if l[i] >= l[j]:
                maxLen[i] = max(maxLen[i], maxLen[j]+1)

    return max(maxLen)


l = [0,8,4,12,2,10,6,14,1,9]
print longestNonDecSubseq(l)

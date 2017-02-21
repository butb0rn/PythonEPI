def applyPermutation(perm, l):
    for i in range(len(l)):
        n = i
        while perm[n] >= 0:
            print l
            l[i], l[perm[n]] = l[perm[n]], l[i]
            temp = perm[n]
            perm[n] = perm[n] - len(perm)
            n = temp

    for i in range(len(perm)):
        perm[i] += len(perm)

    return l


print applyPermutation([2,0,1,3], ["a","b","c","d"])

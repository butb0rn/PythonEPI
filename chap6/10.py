def nextPermutation(perm):

    k = len(perm)-2
    while perm[k] >= perm[k+1]:
        k -= 1

    if k == -1: return None

    for i in range(len(perm)-1, k, -1):
        if perm[i] > perm[k]:
            perm[i], perm[k] = perm[k], perm[i]
            break

    perm[k+1:] = reversed(perm[k+1:])
    return perm

print nextPermutation([6,2,1,5,4,3,0])

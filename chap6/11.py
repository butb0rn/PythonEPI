import random
def randomSampling(l,k):
    for i in range(k):
        r = random.randrange(i,len(l))
        l[i], l[r] = l[r], l[i]
    return l[:k]

l = [1,2,3,4,5,8,9,10,11,12]
print randomSampling(l, 7)

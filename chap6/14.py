from random import randrange

def getRandomSubset(n, k):
    d = {}

    for i in range(k):
        randIdx = i + randrange(n-i)
        ptr1 = d.get(randIdx,-1)
        ptr2 = d.get(i, -1)

        if ptr1 == -1 and ptr2 == -1:
            d[randIdx] = i
            d[i] = randIdx

        elif ptr1 == -1 and ptr2 != -1:
            d[]

import sys

def findClosest(a, b, c):
    diff = sys.maxsize
    p, q, r = len(a), len(b), len(c)
    i = j = k = res_i = res_j = res_k = 0

    while i < p and j < q and k < r:
        maxi = max(a[i], b[j], c[k])
        mini = min(a[i], b[j], c[k])

        if maxi - mini < diff:
            diff = maxi-mini
            res_i, res_j, res_k = i, j, k

        if diff == 0: break

        if a[i] == mini: i+=1
        elif b[j] == mini: j+=1
        elif c[k] == mini: k+=1

    return a[res_i], b[res_j], c[res_k]


print findClosest([5,10,15],[3,6,9,12,15],[8,16,24])

# def findGrayCode(n):
#     def isValid(i,j):
#         return i >> j & 1
#     res = []
#     for i in range(2**n):
#         p = []
#         for j in range(n):
#             p.append(1 if isValid((i>>1)^i,j) else 0)
#         res.append(p)
#
#     return res
#


def findGrayCode(n):
    res = []
    for i in range(1<<n):
        res += bin(i >> 1 ^ i),

    return res

print findGrayCode(3)

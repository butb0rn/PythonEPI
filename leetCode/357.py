'''
Given a non-negative integer n, count all numbers with unique digits.

Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100,
excluding [11,22,33,44,55,66,77,88,99])

'''






def countNumbersWithUniqueDigits(n):
    c = [9,9,8,7,6,5,4,3,2,1]
    res, partial = 1, 1

    for i in range(n):
        partial *= c[i]
        res += partial

    return res


print countNumbersWithUniqueDigits(1)

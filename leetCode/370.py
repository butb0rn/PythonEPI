'''
Assume you have an array of length n initialized with all 0's and are given k update operations.
Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments
each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.
Return the modified array after all k operations were executed.

Example:
Given:

    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
    ]

Output:

    [-2, 0, 3, 5, 3]
'''


def getModifiedArray(updates, length):
    res = [0 for i in range(length)]
    for u in updates:
        res[u[0]] += u[2]
        if u[1]+1 <= length-1:
            res[u[1]+1] -= u[2]

    for r in range(1,length):
        res[r] += res[r-1]

    return res



length = 5
updates = [
    [1,  3,  2],
    [2,  4,  3],
    [0,  2, -2]
]

print getModifiedArray(updates, length)

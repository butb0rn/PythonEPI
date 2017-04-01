def minPathTotal(triangle):
    if not triangle: return 0
    prevRow = triangle[0]
    for i in range(1, len(triangle)):
        curRow = triangle[i]
        curRow[0] += prevRow[0]

        for j in range(1, len(triangle[i])-1):
            curRow[j] += min(prevRow[j], prevRow[j-1])

        curRow[-1] += prevRow[-1]
        prevRow = curRow

    return min(prevRow)


t = [[2],[4,4],[8,5,6],[4,2,6,2],[1,5,2,3,4]]
print minPathTotal(t)

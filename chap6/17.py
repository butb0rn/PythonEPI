import math

def matrixInSpiralOrder(squareMat):
    spiralOrdering = []
    for offset in range(int(math.ceil(len(squareMat) * 0.5))):
        helper(squareMat, offset, spiralOrdering)

    return spiralOrdering


def helper(squareMat, offset, spiralOrdering):

    if (offset == len(squareMat) - offset - 1):
        spiralOrdering.append(squareMat[offset][offset])
        return

    for j in range(len(squareMat) - offset - 1):
        spiralOrdering.append(squareMat[offset][j])

    for i in range(len(squareMat) - offset - 1):
        spiralOrdering.append(squareMat[i][len(squareMat) - offset - 1])

    for j in range(len(squareMat) - offset - 1, offset, -1):
        spiralOrdering.append(squareMat[len(squareMat) - offset - 1][j])

    for i in range(len(squareMat) - offset - 1, offset, -1):
        spiralOrdering.append(squareMat[i][offset])

mat = [[1,2,3],[4,5,6],[7,8,9]]
print matrixInSpiralOrder(mat)

def rotateMat(sqMat):
    matSize = len(sqMat)-1
    for i in range(len(sqMat)/2):
        for j in range(i, matSize-i):
            t1 = sqMat[matSize-j][i]
            t2 = sqMat[matSize-i][matSize-j]
            t3 = sqMat[j][matSize-i]
            t4 = sqMat[i][j]
            sqMat[i][j] = t1
            sqMat[matSize-j][i] = t2
            sqMat[matSize-i][matSize-j] = t3
            sqMat[j][matSize-i] = t4

    return sqMat


mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print rotateMat(mat)

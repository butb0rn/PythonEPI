def numCombinationsForFinalScore(finalScore, plays):
    mat = [[None for i in range(finalScore+1)] for j in range(len(plays))]

    for i in range(len(plays)):
        mat[i][0] = 1
        for j in range(1,finalScore+1):
            withoutThisPlay = mat[i-1][j] if i-1 >= 0 else 0
            withThisPlay = mat[i][j-plays[i]] if j >= plays[i] else 0
            mat[i][j] = withThisPlay + withoutThisPlay

    return mat[len(plays)-1][finalScore]



print numCombinationsForFinalScore(100, [1,5,10,25])

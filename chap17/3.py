def numberOfWays(n, m):
    mat = [[0 for j in range(m)] for i in range(n)]
    return computeNumberOfWays(n-1, m-1, mat)

def computeNumberOfWays(n, m, mat):
    if n == 0 or m == 0: return 1
    if mat[n][m] == 0:
        top = computeNumberOfWays(n-1, m, mat)
        left = computeNumberOfWays(n, m-1, mat)
        mat[n][m] = top+left

    return mat[n][m]

print numberOfWays(5,5)

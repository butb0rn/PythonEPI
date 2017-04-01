def numWaysTop(stairs, steps):
    mat = {}
    def helper(n, steps):
        if n <= 1: return 1

        if n not in mat:
            mat[n] = sum([helper(n-i, steps) for i in range(1,steps+1) if n-i >= 0])

        return mat[n]

    return helper(stairs, steps)

print numWaysTop(4,2)

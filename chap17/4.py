def computeBinomialCoefficient(n,k):
    d = {}
    def helper(n, k):
        if k == 0 or n == k: return 1
        if (n,k) not in d.keys():
            w = helper(n-1,k-1)
            wk = helper(n-1,k)
            d[(n,k)] = w + wk

        return d[(n,k)]

    return helper(n, k)


print computeBinomialCoefficient(5,2)

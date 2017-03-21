def mergeTwoSortedArrays(A, m, B, n):
    a = m-1
    b = n-1
    idx = m+n-1

    while a >= 0 and b >= 0:
        if A[a] >= B[b]:
            A[idx] = A[a]
            a -= 1
        else:
            A[idx] = B[b]
            b -= 1

        idx -= 1

    while b >= 0:
        A[idx] = B[b]
        b -= 1
        idx -= 1

    return A


A = [4,5,8,19,22,None,None,None,None]
B = [3,7,10,26]

print mergeTwoSortedArrays(A, 5, B, len(B))

def mergeArrays(A, B):
    idxA = len(A)-1
    idxB = len(B)-1
    idx = idxA + idxB-1

    while idxA >= 0 and idxB >= 0:
        if A[idxA] > B[idxB]:
            A[idx] = A[idxA]
            idxA -= 1
        else:
            A[idx] = B[idxB]
            idxB -= 1

        idx -= 1

    while idxB >= 0:
        A[idx] = B[idxB]
        idxB -= 1
        idx -= 1

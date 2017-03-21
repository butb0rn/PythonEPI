def levenshteinDistance(a, b):
    mat = [[-1 for j in range(len(b))] for i in range(len(a))]
    def computeDistance(size_a, size_b):
        if size_a < 0: return size_b+1
        if size_b < 0: return size_a+1

        if mat[size_a][size_b] == -1:
            if a[size_a] == b[size_b]:
                mat[size_a][size_b] = computeDistance(size_a-1, size_b-1)
            else:
                substitute = computeDistance(size_a-1, size_b-1)
                add = computeDistance(size_a, size_b-1)
                delete = computeDistance(size_a-1, size_b)
                mat[size_a][size_b] = min(substitute, add, delete) + 1

        return mat[size_a][size_b]

    return computeDistance(len(a)-1, len(b)-1)







print levenshteinDistance("dddfg","p")

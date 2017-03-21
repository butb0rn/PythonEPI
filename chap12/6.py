def matrixSearch(mat, key):
    row = 0
    col = len(mat[0]) - 1
    while row < len(mat) and col >= 0:
        if mat[row][col] == key: return True
        elif mat[row][col] < key: row += 1
        else: col -= 1

    return False

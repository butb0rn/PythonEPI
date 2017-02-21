def nQueens(n):
    result = []
    placeFinder(n, 0, [], result)
    print result
    return result


def placeFinder(n, row, partial, result):
    def isValid(partial):
        rowID = len(partial)-1
        for i in range(rowID):
            diff = abs(partial[i] - partial[rowID])
            if diff == 0 or diff == abs(rowID-i): return False
        return True

    if row == n:
        result.append(list(partial))
    else:
        for col in range(n):
            partial.append(col)
            if isValid(partial):
                placeFinder(n, row+1, partial, result)

            partial.pop()


res = nQueens(4)

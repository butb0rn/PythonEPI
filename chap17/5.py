def isPatternContainedInGrid(grid, pattern):
    previousAttempts = set()
    def isValid(x,y,offset):
        if len(pattern) == offset: return True
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or (x,y,offset) in previousAttempts:
            return False
        if grid[x][y] == pattern[offset] and (isValid(x-1, y, offset+1) or isValid(x+1, y, offset+1) or \
                isValid(x, y+1, offset+1) or isValid(x, y-1, offset+1)):
            return True

        previousAttempts.add((x,y,offset))
        return False

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isValid(i, j, 0):
                return True

    return False


grid = [[1,2,3],[3,4,5],[5,6,7]]
# pattern = [1,3,4,6]
pattern = [1,2,3,4]
print isPatternContainedInGrid(grid, pattern)

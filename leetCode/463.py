class Solution(object):
    def islandPerimeter(self, grid):
        def findEdges(i, j):
            count = 0
            if i > 0 and grid[i-1][j]:
                count += 1
            if i < len(grid)-1 and grid[i+1][j]:
                count += 1
            if j > 0 and grid[i][j-1]:
                count += 1
            if j < len(grid[0])-1 and grid[i][j+1]:
                count += 1
            return count

        h = len(grid)
        w = len(grid[0])
        perimeter = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j]:
                    perimeter += 4 - findEdges(i, j)

        return perimeter


x = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print Solution().islandPerimeter(x)

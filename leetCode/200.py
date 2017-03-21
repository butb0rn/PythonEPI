'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
Example 1:
11110
11010
11000
00000
Answer: 1
'''
class Solution(object):
    def numIslands(self, grid):
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def isValid(grid, i, j):
            return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1"

        def BFS(grid, i, j, visited):
            q = [(i,j)]
            visited.add((i,j))
            while q:
                curr = q.pop(0)
                for d in dir:
                    cell_i = d[0] + curr[0]
                    cell_j = d[1] + curr[1]
                    if not (cell_i, cell_j) in visited and isValid(grid, cell_i, cell_j):
                        visited.add((cell_i, cell_j))
                        q.append((cell_i, cell_j))

        visited = set()
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not (i,j) in visited:
                    visited.add((i,j))
                    BFS(grid, i, j, visited)
                    res += 1
        return res


i = ["11110","11010","11000","00000"]
x = Solution()
print x.numIslands(i)


'''
Nice solution from StefanPochmann
def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
'''

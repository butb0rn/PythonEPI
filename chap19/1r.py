class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Color(object):
    white = 0
    black = 1

class Solution(object):
    def __init__(self):
        self.DIR = [[0,1],[0,-1],[1,0],[-1,0]]

    def getPath(self, maze, startPoint, finishPoint):
        maze[startPoint.x][startPoint.y] = Color.black
        path = [startPoint]

        if (not self.findPath(maze, startPoint, finishPoint, path)):
            path.pop()

        return path

    def isValid(self, maze, cell):
        return cell.x >= 0 and cell.x < len(maze[0]) and cell.y >= 0 and cell.y < len(maze) and \
                maze[cell.x][cell.y] == Color.white

    def findPath(self, maze, s, f, path):
        if s == f: return True
        for d in self.DIR:
            newCell = Coordinate(s.x + d[0], s.y + d[1])
            if self.isValid(maze, newCell):
                maze[newCell.x][newCell.y] = Color.black
                path.append(newCell)
                if self.findPath(maze, newCell, f, path): return True
                path.pop()

        return False


maze = [[0 for j in range(4)] for i in range(4)]
maze[0][1], maze[2][1], maze[3][1], maze[1][3], maze[2][3] = 1,1,1,1,1
res = Solution().getPath(maze, Coordinate(3,0), Coordinate(0,3))
print [(c.x,c.y) for c in res]

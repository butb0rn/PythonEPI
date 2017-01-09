class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def flipColor(maze, cell):
    def isValid(maze, nextCell, color):
        return nextCell.x >= 0 and nextCell.x < len(maze[0]) and \
               nextCell.y >= 0 and nextCell.y < len(maze) and \
               maze[nextCell.x][nextCell.y] == color

    DIR = [[0,1],[0,-1],[1,0],[-1,0]]
    color = maze[cell.x][cell.y]
    maze[cell.x][cell.y] ^= 1
    q = [cell]

    while q:
        curCell = q.pop(0)
        for d in DIR:
            nextCell = Coordinate(curCell.x + d[0], curCell.y + d[1])
            if isValid(maze, nextCell, color):
                maze[nextCell.x][nextCell.y] ^= 1
                q.append(nextCell)

    return maze

def printMaze(maze):
    if maze:
        for i in maze:
            print i

maze = [[1 for j in range(4)] for i in range(4)]
maze[0][0], maze[0][1], maze[0][2] = 0,0,0
maze[2][1], maze[3][1], maze[2][2] = 0,0,0
cell = Coordinate(2,1)
printMaze(maze)
print 
printMaze(flipColor(maze, cell))

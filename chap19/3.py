class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def changeStatus(maze):
    dic = {}
    DIR = [[0,1], [0,-1], [1,0], [-1,0]]
    for i in range(len(maze[0])):
        if maze[0][i] == "w" and (0, i) not in dic.keys():
            markRegion(maze, dic, DIR, 0, i)
        if maze[len(maze)-1][i] == "w" and (len(maze)-1, i) not in dic.keys():
            markRegion(maze, dic, DIR, len(maze)-1, i)

    for i in range(len(maze)):
        if maze[i][0] == "w" and (i, 0) not in dic.keys():
            markRegion(maze, dic, DIR, i, 0)
        if maze[i][len(maze)-1] == "w" and (i, len(maze)-1) not in dic.keys():
            markRegion(maze, dic, DIR, i, len(maze)-1)

    for i in range(len(maze[0])):
        for j in range(len(maze)):
            if maze[i][j] == "w" and (i, j) not in dic.keys():
                maze[i][j] = "b"

    return maze

def markRegion(maze, dic, DIR, row, col):
    dic[(row, col)] = True
    q = []
    cell = Coordinate(row, col)
    q.append(cell)
    while q:
        cell = q.pop(0)
        for d in DIR:
            newCell = Coordinate(cell.x + d[0], cell.y + d[1])
            if newCell.x >= 0 and newCell.x < len(maze[0]) and newCell.y >= 0 and newCell.y < len(maze) and maze[newCell.x][newCell.y] == "w" and (newCell.x, newCell.y) not in dic.keys():
                dic[(newCell.x, newCell.y)] = True
                q.append(newCell)



maze = [["b","b","b","b"],["w","b","w","b"],["b","w","w","b"],["b","b","b","b"]]
newMaze = changeStatus(maze)
for row in newMaze:
    print " ".join(c for c in row)

'''
Search a maze
'''

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False

    def __lt__(self, other):
        if self.x != other.x or self.y != other.y: return False
        return True


class Solution(object):
    def __init__(self):
        self.directions = [[0,1],[0,-1], [1,0], [-1,0]]

    def getPath(maze, start, finish):
        path = []
        self.findPath(maze, start, finish, path)
        return path

    def isValid(maze, cell):
        return cell.x > 0 and cell.x < len(maze[0]) and cell.y > 0 and cell.y < len(maze) and not cell.visited

    def findPath(maze, cell, finish, path):
        if cell == finish : return True
        for d in self.directions:
            newCell = Coordinate(cell.x + d.x, cell.y + d.y)
            if self.isValid(newCell):
                newCell.visited = True
                path.append(newCell)
                if self.findPath(maze, newCell, finish): return True
                partial.pop()

        return False

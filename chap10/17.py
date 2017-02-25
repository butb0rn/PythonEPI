class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.locked = False
        self.numLockedDescendants = 0

    def isLocked(self):
        return self.locked

    def lock(self):
        if self.numLockedDescendants > 0 or self.locked: return False

        t = self.parent
        while t:
            if (t.isLocked()): return False
            t = t.parent

        self.locked = True

        p = self.parent
        while p:
            p.numLockedDescendants += 1
            p = p.parent

        return True

    def unlock(self):
        if (self.locked):
            self.locked = False
            p = self.parent
            while p:
                p.numLockedDescendants -= 1
                p = p.parent

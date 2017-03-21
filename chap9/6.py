def getBuildingWithSunset(buildings):
    s = []
    idx = len(buildings)-1
    while idx >= 0:
        curBuilding = buildings[idx]
        while s and curBuilding >= s[-1]:
            s.pop()
        s.append(curBuilding)
        idx -= 1
    return s

b = [8, 7, 9, 12, 3, 16, 30, 2]
print getBuildingWithSunset(b)

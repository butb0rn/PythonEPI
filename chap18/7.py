def getMaxTrappedWater(heights):
    area, leftSide, rightSide = 0, 0, len(heights)-1

    while leftSide < rightSide:
        area = max(area, (rightSide - leftSide) * min(heights[leftSide], heights[rightSide]))
        if heights[leftSide] == heights[rightSide]:
            leftSide += 1
            rightSide -= 1
        elif heights[leftSide] < heights[rightSide]:
            leftSide += 1
        else:
            rightSide -= 1

    return area

heights = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
print getMaxTrappedWater(heights)

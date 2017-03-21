def largestRecArea(heights):
    s, maxArea = [], 0
    def isValid(curIdx, stackIdx):
        return heights[curIdx] < heights[stackIdx] if curIdx < len(heights) else True

    for i in range(len(heights)+1):
        while s and isValid(i, s[-1]):
            height = heights[s.pop()]
            width = i if not s else i - s[-1] -1
            maxArea = max(maxArea, height * width)

        s.append(i)
    return maxArea


heights = [1,4,4,2,5,6,3,2,6,6,2,1,3,3]
print largestRecArea(heights)

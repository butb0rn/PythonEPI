class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    # def insert(self, intervals, newInterval):
    #     out = []
    #     for i in intervals:
    #         if i.end < newInterval.end:
    #             out.append(i)
    #         elif newInterval.end < i.start:
    #             out.append(newInterval)
    #             newInterval = i
    #         elif i.end >= newInterval.start or i.start <= newInterval.end:
    #             newInterval = Interval(min(i.start, newInterval.start), max(i.end, newInterval.end))
    #
    #     out.append(newInterval)
    #     return out


    def insert(self, intervals, newInterval):
        s, e = newInterval.start, newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[~len(right)].end)
        return left + [Interval(s, e)] + right


# i = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)]
i = [Interval(1,2), Interval(6,7)]
res = Solution().insert(i, Interval(3,6))
for i in res:
    print str(i.start) + " - " + str(i.end)

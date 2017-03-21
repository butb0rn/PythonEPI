class Event(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def mergeIntervals(intervals, interval):
    res = []
    intervals.append(interval)
    for i in sorted(intervals, key=lambda x: x.start):
        if res and i.start <= res[-1].end:
            res[-1].end = max(res[-1].end, i.end)
        else:
            res += i,

    return res


intervals = [Event(-4, -1), Event(0, 2), Event(3, 6), Event(7, 9), Event(11, 12), Event(14, 17)]
print [(i.start, i.end) for i in mergeIntervals(intervals, Event(1,8))]

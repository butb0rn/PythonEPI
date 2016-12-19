# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out

res = merge([Interval(1,3),Interval(15,18), Interval(2,6),Interval(8,10)])
for interval in res:
    print str(interval.start) + "-" + str(interval.end)

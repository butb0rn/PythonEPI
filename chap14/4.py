# def minMeetingRooms(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: int
#         """
#         minHeap = []
#         e = sorted(intervals, key=lambda x: x.start)
#         for i in e:
#             if minHeap and i.start >= minHeap[0]:
#                 heapreplace(minHeap, i.end)
#             else:
#                 heappush(minHeap, i.end)
#
#         return len(minHeap)

class Event(object):
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish


class EndPoint(object):
    def __init__(self, time, isStart):
        self.time = time
        self.isStart = isStart

    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time

        if not self.isStart: return True

        return False


def findMaxEvents(events):
    e = []
    for i in events:
        e.append(EndPoint(i.start, True))
        e.append(EndPoint(i.finish, False))

    e.sort()
    maxEvent, counter = 0, 0
    for point in e:
        if point.isStart:
            counter += 1
            maxEvent = max(maxEvent, counter)
        else:
            counter -= 1

    return maxEvent

#e = [Event(1,5), Event(2,7), Event(4,5), Event(6,10), Event(6,10), Event(9,17), Event(11,13), Event(12,15), Event(14,15)]
e = [Event(0, 30),Event(5, 10),Event(15, 20)]
print findMaxEvents(e)

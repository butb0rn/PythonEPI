import unittest

class Interval(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right


def findMinVisits(intervals):
    if not intervals: return None
    visits = []
    for interval in sorted(intervals, key=lambda i: i.right):
        if not visits: visits.append(interval.right)
        if interval.left > visits[-1]: visits.append(interval.right)

    return visits


class TestFindMinVisits(unittest.TestCase):
    def test_two_min(self):
        tasks = [Interval(0,3), Interval(2,6), Interval(3,4), Interval(6,9)]
        self.assertEqual(findMinVisits(tasks), [3,9])

    def test_more(self):
        tasks = [Interval(1,2), Interval(2,3), Interval(3,4), Interval(2,3), Interval(3,4), Interval(4,5)]
        self.assertEqual(findMinVisits(tasks), [2,4])








if __name__ == '__main__': unittest.main()

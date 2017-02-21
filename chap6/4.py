import unittest

def canReachEnd(l):
    soFar = 0
    lastIndex = len(l)-1
    idx = 0
    while (idx <= soFar and soFar < lastIndex):
        soFar = max(soFar, idx+l[idx])
        idx+=1

    return soFar >= lastIndex


class TestCanReachEnd(unittest.TestCase):
    def test_can_reach_end(self):
        l = [3,3,1,0,2,0,1]
        self.assertEqual(canReachEnd(l), True)

    def test_can_not_reach_end(self):
        l = [3,2,0,0,2,0,1]
        self.assertEqual(canReachEnd(l), False)



if __name__ == '__main__': unittest.main()

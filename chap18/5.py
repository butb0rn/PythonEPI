import unittest

def findMajorityString(l):
    if not l: return None
    element = ""
    idx, counter = 0, 0

    while idx < len(l):
        if counter == 0:
            element = l[idx]
            counter += 1
        elif l[idx] == element:
            counter += 1
        else:
            counter -= 1

        idx += 1

    return element

class TestFindMajority(unittest.TestCase):

    def test_a_is_majority(self):
        l = ["b","a","c","a","a","b","a","a","c","a"]
        self.assertEqual(findMajorityString(l),"a")

    def test_last_one_is_majority(self):
        l = ["b","a","c"]
        self.assertEqual(findMajorityString(l),"c")





if __name__ == '__main__': unittest.main()

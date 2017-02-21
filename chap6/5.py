import unittest

def deleteDuplicates(l):
    if not l: return None

    writeIdx = 1
    for i in range(1, len(l)):
        if (l[writeIdx-1] != l[i]):
            l[writeIdx] = l[i]
            writeIdx +=1

    return l

class TestDeleteDuplicates(unittest.TestCase):
    def test_empty_arr(self):
        l = []
        self.assertEqual(deleteDuplicates(l), None)

    def test_with_no_dup(self):
        l = [1,2,3,4,5,6]
        eRes = [1,2,3,4,5,6]
        self.assertEqual(deleteDuplicates(l), eRes)

    def test_with_dups(self):
        l = [2,3,5,5,7,11,11,11,13]
        eRes = [2,3,5,7,11,13,11,11,13]
        self.assertEqual(deleteDuplicates(l), eRes)



if __name__ == '__main__': unittest.main()
# print deleteDuplicates([2,3,5,5,7,11,11,11,13])

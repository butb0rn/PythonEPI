import unittest

def isPalindromic(s):
    s = filter(lambda x: x.isalpha(), s)
    i,j = 0, len(s)-1

    while i <= j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1

    return True

class TestIsPalindromic(unittest.TestCase):

    def test_empty_input(self):
        s = ""
        self.assertEqual(isPalindromic(s), True)

    def test_not_alphabetic_input(self):
        s = "123!!2@09"
        self.assertEqual(isPalindromic(s), True)

    def test_palindromic(self):
        s = "b1c!b"
        self.assertEqual(isPalindromic(s), True)

    def test_not_palindromic(self):
        s = "b1c!bb"
        self.assertEqual(isPalindromic(s), False)









if __name__ == '__main__': unittest.main()

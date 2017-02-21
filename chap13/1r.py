import unittest

def isPalindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]: return False
        left += 1
        right -= 1

    return True


class MyTest(unittest.TestCase):

    def test_not_a_palindrome_string(self):
        self.assertEqual(isPalindrome("bcbd"), False)

    def test_is_a_palindrome_string(self):
        self.assertEqual(isPalindrome("level"), True)


if __name__ == "__main__": unittest.main()

class Solution(object):
    def __init__(self):
        self.letters = [[],[],["a","b","c"],["d","e","f"], ["g","h","i"], ["j","k","l"], ["m","n","o"], ["p","q","r","s"],["t","u","v"], ["w","x","y","z"]]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        return self.getLetters(digits, 0)


    def getLetters(self, nums, idx):
        result = []
        if idx > len(nums)-1:
            return []
        num = nums[idx]
        partial = self.getLetters(nums, idx+1)
        for l in self.letters[int(num)]:
            result += [l+x for x in partial] or l

        return result


x = Solution()
print x.letterCombinations("23")

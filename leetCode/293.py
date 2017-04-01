class Solution(object):
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s)-1):
            if s[i:i+2]=='++':
                res += [s[:i]+'--'+s[i+2:]]
        return res

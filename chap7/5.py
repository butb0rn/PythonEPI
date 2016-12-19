def isPalindromic(exp):
    def isalpha(exp):
        return exp.isalpha()
    exp = map(lambda x: x.lower(), filter(isalpha, exp))
    rIdx = len(exp)-1
    for idx in range(len(exp)):
        if exp[idx] != exp[rIdx]:
            return False
        rIdx -= 1
    return True

s = "A man, a plan, a canal, Panama."
#s = "a b c"
print isPalindromic(s)

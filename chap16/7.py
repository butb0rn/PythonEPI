def generatePalindromicDecomposition(s):
    result = []
    decompositionHelper(s, 0, [], result)
    return result


def decompositionHelper(s, offset, partialResult, result):
    if offset == len(s):
        result.append(partialResult[:])
        return

    for i in range(offset+1, len(s)+1):
        prefix = s[offset:i]
        if isPalindromic(prefix):
            partialResult.append(prefix)
            decompositionHelper(s, i, partialResult, result)
            partialResult.pop()


def isPalindromic(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1

    return True


print generatePalindromicDecomposition("0204451881")

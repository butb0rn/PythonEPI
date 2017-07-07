def findAllSubstrings(s, words):
    generalWordToFreq = {}
    for w in words:
        increment(w, generalWordToFreq)

    unitSize = len(words[0])
    result = []
    for i in range(len(s)):
        if (i + unitSize*len(words) <= len(s)) and isValid(s, generalWordToFreq, i, len(words), unitSize):
            result.append(i)

    return result

def isValid(s, wordToFreq, start, numWords, unitSize):
    currStringToFreq = {}
    for i in range(numWords):
        sIdx = start + i*unitSize
        fIdx = start + (i+1)*unitSize
        currWord = s[sIdx:fIdx]
        freq = wordToFreq.get(currWord, 0)
        if freq == 0:
            return False
        increment(currWord, currStringToFreq)
        if currStringToFreq[currWord] > freq:
            return False

    return True

def increment(word, d):
    count = d.get(word, 0)
    d[word] = count + 1

s = "amanaplanacanalaliamanaplanacanal"
words = ["can","apl","ana"]
print findAllSubstrings(s, words)

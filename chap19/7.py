class Candidate(object):
    def __init__(self, label, distance=0):
        self.label = label
        self.distance = distance


def transformString(d, s, t):
    q = [Candidate(s, 0)]
    d.discard(s)

    while q:
        f = q.pop(0)
        if f.label == t: return f.distance
        word = f.label
        for i in range(len(word)):
            start = word[0:i]
            end = word[i+1:]
            for j in range(26):
                newString = start + chr(ord('a')+j) + end
                if newString in d:
                    d.discard(newString)
                    q.append(Candidate(newString,f.distance+1))

    return -1

s = set(["bat", "cot", "dog", "dag", "dot", "cat"])
print transformString(s, "cat", "dog")

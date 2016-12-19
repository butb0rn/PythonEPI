def removeDup(s):
    s.sort()
    crr = 0
    i = 1
    while i < len(s):
        if s[crr] != s[i]:
            crr+=1
            s.insert(crr, s[i])
        i+= 1
    return s[:crr+1]

#['bb', 'cc', 'cc', 'cc', 'dd', 'eh', 'eh', 'eh', 'f']
print removeDup(["eh","eh", "cc", "bb", "cc", "eh", "dd", "f", "cc"])

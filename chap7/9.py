def romanToInteger(s):
    di = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    res = di[s[len(s)-1]]
    for i in range(len(s)-2, -1,-1):
        print i, i+1
        if di[s[i]] < di[s[i+1]]:
            res -= di[s[i]]
        else:
            res += di[s[i]]

    return res

print romanToInteger("LVIIII")

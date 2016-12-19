def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    t = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and r[s[i]] < r[s[i+1]]:
            t += r[s[i+1]] - r[s[i]]
            i += 1
        else:
            t += r[s[i]]

        i+= 1
    return t


print romanToInt("DCXXI")

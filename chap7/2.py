def convertBase(s, b1, b2):
    p = number = 0
    res = []
    for i in range(len(s)-1, -1, -1):
        number += (ord(s[i])-ord('0'))*(b1**p)
        p+=1

    while number > 0:
        r = number % b2
        if r >= 10:
            res.append(chr(r + ord('A') - 10))
        else:
            res.append(chr(r+ord('0')))
        number /= b2
    res.reverse()
    return "".join(res)


print convertBase("615", 7, 13)

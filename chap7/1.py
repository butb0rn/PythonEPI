def intToString(num):
    res = []
    isNeg = False

    if num < 0:
        num = -1 * num
        isNeg = True

    while num > 0:
        r = num % 10
        num /= 10
        res.append(chr(r+ord('0')))

    res.reverse()
    if isNeg: res.insert(0,'-')

    return "".join(res)

def stringToInt(numList):
    num = 0
    start = 0
    isNeg = False
    if numList[0] == '-':
        start = 1
        isNeg = True

    for l in range(start, len(numList)):
        num = num*10 + ord(numList[l]) - ord('0')

    if isNeg: num = -num
    return num


print stringToInt("23456")

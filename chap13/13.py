def isCollatzConjecture(n):
    verifiedNums = set()

    for i in range(3,n+1,2):
        helperSet = set()
        num = i

        while num >= i:
            if num in helperSet: return False
            else: helperSet.add(num)

            if num % 2 != 0:
                if num in verifiedNums:
                    break
                else:
                    verifiedNums.add(num)
                newNum = num * 3 + 1
                if newNum <= num:
                    print "overflow for" + str(newNum)
                    break
                num = newNum
            else:
                num /= 2
    return True

print isCollatzConjecture(11)

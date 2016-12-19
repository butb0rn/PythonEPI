def findSpreadsheetEncoding(l):
    result = 0; base = 26; crr = len(l)-1
    alpha = 'ABCDEFGGIJKLMNOPQRSTUVWXYZ'

    for idx in range(len(l)):
        item = l[idx]
        result += (alpha.find(item)+1)*(base**crr)
        crr -= 1
    return result

print findSpreadsheetEncoding("AA")

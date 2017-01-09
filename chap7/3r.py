#FIRST PART

def getSheetNumber(col):
    if not col: return None
    number = 0
    for l in col:
        number = number * 26 + ord(l) - ord('A') + 1
    return number

print getSheetNumber("AA")

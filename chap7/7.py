def phoneMnemonic(phoneNumber):
    letters = [[],[],["a","b","c"],["d","e","f"], ["g","h","i"], ["j","k","l"], \
                    ["m","n","o"], ["p","q","r","s"],["t","u","v"], ["w","x","y","z"]]

    def phoneMnemonicHelper(phoneNumber, idx):
        if idx > len(phoneNumber)-1: return []
        result = []
        partial = phoneMnemonicHelper(phoneNumber, idx+1)
        for l in letters[int(phoneNumber[idx])]:
            result += [l+x for x in partial] or l
            print result
        return result

    return phoneMnemonicHelper(phoneNumber, 0)



print phoneMnemonic("23")

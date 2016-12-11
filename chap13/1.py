def isPalindromic(word):
    dic = {}
    oddCount = 0
    for letter in word:
        if letter in dic.keys():
            dic[letter] = dic[letter] + 1
            if dic[letter] % 2 != 0:
                oddCount += 1
            else:
                oddCount -= 1
        else:
            dic[letter] = 1
            oddCount += 1

    if oddCount > 1:
        return False

    return True

# edilklied -> True
# ediopied  -> False
print isPalindromic("ediopied")

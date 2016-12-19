def reverseWords(sen):
    result = []
    sen = sen.split(' ')
    for idx in range(len(sen)-1,-1,-1):
        result.append(sen[idx])

    return " ".join(result)

s = "Bob likes Alice"
print reverseWords(s)

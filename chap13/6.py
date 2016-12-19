def findNearestEntries(exp):
    dic = {}
    for idx in range(len(exp)):
        if exp[idx] in dic.keys():
            item = dic[exp[idx]]
            if (item[0] == -1):
                dic[exp[idx]] = (item[1], idx)
            elif (idx - item[1] <= item[1] - item[0]):
                dic[exp[idx]] = (item[1], idx)
        else:
            dic[exp[idx]] = (-1,idx)

    for key, value in dic.items():
        if value[0] == -1:
            del dic[key]
    print dic

s = ["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "result"]
findNearestEntries(s)

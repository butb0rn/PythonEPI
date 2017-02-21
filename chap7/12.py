def encode(s):
    result = []
    count = 1
    for i in range(1,len(s)+1):
        if i == len(s) or s[i] != s[i-1]:
            result.append(str(count)+s[i-1])
            count = 1
        else:
            count += 1

    return "".join(result)


def decode(s):
    i = 0
    result = []
    while i < len(s):
        c = s[i]
        l = s[i+1]
        result.append(int(c)*l)
        i += 2
    return "".join(result)

print encode("eeeffffee")
print decode("3e4f2e")

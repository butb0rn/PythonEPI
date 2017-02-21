def getValidIpAddress(s):
    def isValidIp(ip):
        if len(ip) > 3: return False
        if ip[0] == "0" and len(ip) > 1: return False

        validIp = int(ip)
        return validIp <= 255 and validIp >= 0

    result = []
    for i in range(1,4):
        if i < len(s):
            first = s[:i]
            if isValidIp(first):
                for j in range(1,4):
                    if i+j < len(s):
                        second = s[i: i+j]
                        if isValidIp(second):
                            for k in range(1,4):
                                if i+j+k < len(s):
                                    third = s[i+j:i+j+k]
                                    forth = s[i+j+k:]
                                    if isValidIp(third) and isValidIp(forth):
                                        result.append(".".join([first,second,third,forth]))
    return result

print getValidIpAddress("19216811")

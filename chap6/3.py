def multiply(num1, num2):
    if not num1 or not num2: return None
    if num1[0] ^ num2[0] < 0:
        sign = -1
    else:
        sign = 1

    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0]*(len(num1)+len(num2))
    for i in range(len(num1)-1,-1,-1):
        for j in range(len(num2)-1,-1,-1):
            result[i+j+1] += num1[i] * num2[j]
            result[i+j] += result[i+j+1]/10
            result[i+j+1] = result[i+j+1]%10


    not_zero = 0
    while not_zero < len(result) and result[not_zero] == 0:
        not_zero += 1
    result = result[not_zero:]

    if not result: return None
    result[0] *= sign
    return result



print multiply([1,9,3,7,0,7,7,2,1],[-7,6,1,8,3,8,2,5,7,2,8,7])

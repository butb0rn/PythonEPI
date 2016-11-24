def evaluate_exp(exp):
    stack = []
    for element in exp:
        if element.isdigit():
            stack.append(element)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if element == "+":
                stack.append(int(op1)+int(op2))
            elif element == "-":
                stack.append(int(op1)-int(op2))
            elif element == "/":
                stack.append(int(op1)/int(op2))
            elif element == "*":
                stack.append(int(op1)*int(op2))

    return stack.pop()


exp = "34+2*1+"
print evaluate_exp(exp)

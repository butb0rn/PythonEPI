def rpnEval(exp):
    if not exp: return None
    s = []
    for e in exp:
        if e.isdigit():
            s.append(e)
        elif e == "+":
            op1 = int(s.pop())
            op2 = int(s.pop())
            s.append(op1+op2)

        elif e == "-":
            op1 = int(s.pop())
            op2 = int(s.pop())
            s.append(op1-op2)

        elif e == "*":
            op1 = int(s.pop())
            op2 = int(s.pop())
            s.append(op1*op2)

        elif e == "/":
            op1 = int(s.pop())
            op2 = int(s.pop())
            s.append(op1/op2)

    return s.pop()


print rpnEval(["3","4","+","2","*","1","+"])

def isWellFormed(s):
    stack = []
    for i in s:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":
            if not stack: return False
            if i == "}" and stack[-1] == "{":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == ")" and stack[-1] == "(":
                stack.pop()

    return not stack

print isWellFormed("[()]()()[]")

def is_well_formedness(exp):
    stack = []
    left_side = "({["
    right_side = ")}]"
    for element in exp:
        if element in left_side:
            stack.append(element)
        elif len(stack) < 1 or left_side.index(stack[-1]) != right_side.index(element):
            return False
        else:
            stack.pop()

    if len(stack) > 0:
        return False

    return True


print is_well_formedness("[])}][]")

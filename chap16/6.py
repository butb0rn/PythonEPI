def generateMatchedParens(k):
    def parensHelper(left, right, partial, result):
        if left == 0 and right == 0:
            result.append("".join(partial[:]))
            return

        if left > 0:
            partial.append("(")
            parensHelper(left-1, right, partial, result)
            partial.pop()

        if left < right:
            partial.append(")")
            parensHelper(left, right-1, partial, result)
            partial.pop()


    result = []
    parensHelper(k, k, [], result)
    return result


print generateMatchedParens(4)

def isProper(n0, n1, middle):
    s0, s1 = n0, n1

    while s0.data != n1.data and s0.data != middle.data and s1.data != n0.data and s1.data != middle.data \
            and not s0.data or not s1.data:
        if s0:
            if s0.data > middle.data:
                s0 = s0.left
            else:
                s0 = s0.right

        if s1:
            if s1.data > middle.data:
                s1 = s1.left
            else:
                s1 = s1.right


    if s0.data == n1.data or s1.data == n0.data or (s0.data != middle.data and s1.data != middle.data):
        return False

    if s0.data == middle.data:
        return searchTarget(middle, s1)
    else:
        return searchTarget(middle, s0)


def searchTarget(f, t):

    while f and f.data != t.data:
        if f.data > t.data:
            f = f.left
        else:
            f = f.right

    return f.data == t.data

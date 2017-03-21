def setJumpOrder(l):
    if not l: return None

    order = 0
    s = [l]
    while s:
        cur = s.pop()
        while cur and cur.order == -1:
            cur.order = order
            order += 1
            s.append(cur.next)
            s.append(cur.jump)



def setJumpOrder(l, order):
    if l and order != -1:
        l.order = order
        order += 1
        order = setJumpOrder(l.jump, order)
        order = setJumpOrder(l.next, order)

    return order

class LinkedList(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

def removeDups(l):
    cur = prev = l.next
    while cur:
        if cur.data != prev.data:
            prev.next = cur
            prev = cur
            cur = cur.next
        else:
            cur = cur.next

    return l.next


l = LinkedList(0, LinkedList(1, LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(4)))))))
res = removeDups(l)
while res:
    print res.data

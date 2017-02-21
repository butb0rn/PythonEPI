class LinkedList(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode


def removeKthLast(l, k):
    first = dummy = l
    first = first.next
    while k > 0:
        first = first.next
        k -= 1

    second = dummy
    while first:
        first = first.next
        second = second.next

    second.next = second.next.next

    return dummy.next


a = LinkedList("a")
b = LinkedList("b")
c = LinkedList("c")
d = LinkedList("d")
e = LinkedList("e")
f = LinkedList("f")

head = LinkedList(0, a)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

res = removeKthLast(head, 2)
while res:
    print res.data
    res = res.next

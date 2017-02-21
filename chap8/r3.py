class LinkedList(object):
    def __init__(self, data, nextNode=None):
        self.data = data
        self.next = nextNode

def hasCycle(l):
    if not l: return None
    fast = slow = l
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            slow = l
            while slow and slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    return None


a = LinkedList("a")
b = LinkedList("b")
c = LinkedList("c")
d = LinkedList("d")
g = LinkedList("g")
h = LinkedList("h")

head = LinkedList(0, a)
a.next = b
b.next = c
c.next = d
d.next = g
g.next = h
h.next = c

# print hasCycle(head)

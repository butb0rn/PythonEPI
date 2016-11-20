class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Solution:

    def find_cyclicity(self, l):
        if l == None:
            return None
        count = 0
        fast = slow = l
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
            if (fast == slow):
                slow = prev = l
                while (slow != fast):
                    prev = fast
                    slow = slow.next
                    fast = fast.next
                    count += 1

                prev.next = None
                print "Length is => " + str(count)
                print "Cycle starts from => " + str(slow.value)
                return l

        return l


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)
node_4 = ListNode(4)
node_5 = ListNode(5)
node_6 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5
node_5.next = node_6
node_6.next = node_4
x = Solution()

res = x.find_cyclicity(node_1)
while res:
    print res.value
    res = res.next

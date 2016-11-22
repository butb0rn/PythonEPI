class ListNode:
    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node

class Solution:

    def add_lists(self, l1, l2):
        if l1 == None and l2 == None:
            return None

        carrier = 0
        partial_res = ListNode()
        result = partial_res

        while l1 or l2:

            if l1:
                carrier += l1.value
                l1 = l1.next

            if l2:
                carrier += l2.value
                l2 = l2.next

            partial_res.next = ListNode(carrier%10)
            carrier /= 10
            partial_res = partial_res.next

        if carrier == 1:
            partial_res.next = ListNode(1)

        return result.next


l1 = ListNode(3, ListNode(1, ListNode(4)))
l2 = ListNode(7, ListNode(0, ListNode(9)))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
res = sol.add_lists(l1, l2)
while res:
    print'{} =>'.format(res.value),
    res = res.next
print None

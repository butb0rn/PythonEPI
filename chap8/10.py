class ListNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Solution:

    def merge_even_odd(self, l):
        q = l
        dummy_even = even_nodes = ListNode(0)
        dummy_odd = odd_nodes = ListNode(0)

        while q:
            if q.value % 2 == 0:
                even_nodes.next = q
                even_nodes = q
            else:
                odd_nodes.next = q
                odd_nodes = q

            q = q.next

        odd_nodes.next = None
        l = dummy_even.next
        even_nodes.next = dummy_odd.next

        return l

x = ListNode(1, ListNode(3, ListNode(2, ListNode(4, ListNode(5, ListNode(7, ListNode(8, ListNode(6, ListNode(0)))))))))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
res = sol.merge_even_odd(x)
while res:
    print res.value
    res = res.next

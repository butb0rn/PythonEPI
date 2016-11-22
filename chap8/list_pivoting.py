class ListNode:
    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node

class Solution:

    def update_list(self, l, k):
        dummy_great = greater = ListNode()
        dummy_less = less = ListNode()
        dummy_equal = equal = ListNode()
        q = l
        while q:
            if q.value < k:
                less.next = q
                less = q
            elif q.value == k:
                equal.next = q
                equal = q
            else:
                greater.next = q
                greater = q

            q = q.next

        greater.next = None
        less.next = dummy_equal.next
        equal.next = dummy_great.next

        return dummy_less.next

x = ListNode(4, ListNode(10, ListNode(1, ListNode(6, ListNode(11, ListNode(3, ListNode(2, ListNode(9, ListNode(5)))))))))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
res = sol.update_list(x, 5)
while res:
    print res.value
    res = res.next

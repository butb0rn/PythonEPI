class ListNode:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Solution:

    def get_r_shift_list(self, l, k):
        if k == 0:
            return l
        len_l = self.get_len(l)
        step = len_l - k
        q = l
        while step > 1:
            q = q.next
            step -= 1

        p = q.next
        q.next = None
        dummy = p

        while p.next:
            p = p.next

        p.next = l

        return dummy

    def get_len(self, l):
        count = 0
        while l:
            l = l.next
            count += 1

        return count


x = ListNode(2, ListNode(3, ListNode(5, ListNode(3, ListNode(2)))))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
# res = sol.remove_dup_sorted_list(x)
res = sol.get_r_shift_list(x, 4)
while res:
    print res.value
    res = res.next

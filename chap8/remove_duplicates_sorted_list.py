class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Solution:

    def remove_dup_sorted_list(self, l):
        q = l
        while q:
            p = q.next
            while (p) and (p.value == q.value):
                p = p.next

            q.next = p
            q = p
        return l

    def remove_dup_elements_included(self, l):
        q = l
        flag = False
        while q:
            p = q.next
            while (p) and (p.value == q.value):
                p = p.next
                flag = True

            if flag:
                q.value = p.value
                q.next = p.next
                flag = False
            else:
                q.next = p
                q = p
        return l


x = ListNode(1, ListNode(1, ListNode(3, ListNode(3, ListNode(6, ListNode(6, ListNode(7, ListNode(7, ListNode(7, ListNode(8, ListNode(9)))))))))))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
# res = sol.remove_dup_sorted_list(x)
res = sol.remove_dup_elements_included(x)
while res:
    print res.value
    res = res.next

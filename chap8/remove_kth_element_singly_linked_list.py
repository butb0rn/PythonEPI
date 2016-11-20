class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Solution:
    def remove_kth_element(self, l, k):
        fast = slow = l
        while k > 0:
            fast = fast.next
            k -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return l

x = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
sol = Solution()
res = sol.remove_kth_element(x, 6)
while res:
    print res.value
    res = res.next

class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class Solution:

    def is_palindromic(self, l):
        fast = slow = l
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        fast = self.get_reverse_list(slow)
        slow = l

        while slow and fast:
            if slow.data != fast.data:
                return False
            slow = slow.next
            fast = fast.next

        return True

    def get_reverse_list(self, l):
        prev = None
        q = l

        while q:
            temp = q.next
            q.next = prev
            prev = q
            q = temp

        return prev


x = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
print sol.is_palindromic(x)

"""
Take a singly linked list L and two integers s and f as arguments,
and reverse the order of the nodes from the sth node to fth node.
"""

class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Solution:

    def reverse_list(self, list_node):
        if list_node == None:
            return

        prev = None
        res = list_node
        q = list_node

        while q:
            temp = q.next
            q.next = prev
            prev = q
            q = temp

        return prev


    def reverse_sublist(self, list_node, start, finish):

        if start == finish:
            return list_node

        dummy_head = list_node
        count = 1

        while (count < start):
            dummy_head = dummy_head.next
            count += 1

        prev = dummy_head
        q = dummy_head.next

        while (start < finish):
            start += 1
            temp = q.next
            q.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return list_node

x = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
sol = Solution()
#res = sol.reverse_sublist(x, 0, 4)
res = sol.reverse_list(x)
while res:
    print res.value
    res = res.next

'''
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        def reverseList(self, head):
            cur = head
            prev = None
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            return prev

        revHead = reverseList(self, head)
        cur = revHead
        car = 1
        dummy = res = ListNode(0)
        while cur:
            car += cur.val
            dummy.next = ListNode(car%10)
            car /= 10
            dummy = dummy.next
            cur = cur.next
        if car > 0:
            dummy.next = ListNode(1)
            dummy = dummy.next

        return reverseList(self, res.next)

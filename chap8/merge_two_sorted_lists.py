"""
Consider two singly linked list in which each node holds a number.
return a new linked list that contains both linkedlist and it is sorted.
"""

import unittest

class Node:
    def __init__(self, data, n=None):
        self.data = data
        self.next = n

class Solution:
    def merge_two_lists(self, l1, l2):
        p1,p2 = l1,l2
        q = Node(0)
        result = q
        while p1 and p2:
            if p1.data < p2.data:
                q.next = p1
                p1 = p1.next
            else:
                q.next = p2
                p2 = p2.next
            q = q.next

        if p1:
            q.next = p1
    
        if p2:
            q.next = p2

        return result.next

class MergeTwoListsTests(unittest.TestCase):
    def testOneMergeL1andL2(self):
        l1 = Node(1, Node(4))
        l2 = Node(3, Node(5, Node(7)))
        funci = Solution()
        expected_result = Node(1, Node(3, Node(4, Node(5, Node(7)))))
        actual_result = funci.merge_two_lists(l1,l2)
        while actual_result:
            self.assertEqual(actual_result.data,expected_result.data)
            actual_result = actual_result.next
            expected_result = expected_result.next


def main():
    unittest.main()

if __name__ == "__main__":
    main()

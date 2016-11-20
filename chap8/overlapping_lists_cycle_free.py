class ListNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Solution:
    def find_node(self, l1, l2):

        l1_len = self.get_len(l1)
        l2_len = self.get_len(l2)

        p1 = l1
        p2 = l2
        if l1_len > l2_len:
            p1 = self.adjusted_list(l1_len - l2_len, l1)
        else:
            p2 = self.adjusted_list(l2_len - l1_len, l2)

        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1

    def get_len(self, node_list):
        count = 0
        while node_list:
            count += 1
            node_list = node_list.next

        return count


    def adjusted_list(self, diff, input_list):
        while (diff > 0):
            diff -= 1
            input_list = input_list.next

        return input_list


node_1 = ListNode(1)
node_2 = ListNode(2)
node_3 = ListNode(3)

node_4 = ListNode(4)
node_5 = ListNode(5)

node_6 = ListNode(6)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_6

node_4.next = node_5
node_5.next = node_6
node_6.next = None
x = Solution()

res = x.find_node(node_1, node_4)
print res.data if res else None

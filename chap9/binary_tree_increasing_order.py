def get_binary_tree(tree):
    dic = {}
    if tree:
        tree.level = 0
    q = [tree]

    while q:
        node = q.pop(0)

        if node.right:
            node.right.level = node.level + 1
            q.append(node.right)

        if node.left:
            node.left.level = node.level + 1
            q.append(node.left)

        if len(dic) > node.level:
            temp = dic[node.level]
            temp.append(node)
        else:
            dic[node.level] = [node]

    for val in dic.values():
        print ",".join(str(i.data) for i in val)




class ListNode:
    def __init__(self, data=None, right_child=None, left_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child
        self.level = 0

tree = ListNode(314, ListNode(6, ListNode(271), ListNode(561, None, ListNode(3, ListNode(17)))), ListNode(6, ListNode(2), ListNode(28)))
get_binary_tree(tree)

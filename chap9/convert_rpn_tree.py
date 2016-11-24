class ListNode:
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.right = right_child
        self.left = left_child


def get_tree(exp):
    stack = []
    for element in exp:
        if element.isdigit():
            stack.append(element)
        else:
            if isinstance(stack[-1], ListNode):
                op2 = stack.pop()
            else:
                op2 = ListNode(stack.pop())

            if isinstance(stack[-1], ListNode):
                op1 = stack.pop()
            else:
                op1 = ListNode(stack.pop())

            stack.append(ListNode(element, op1, op2))

    if len(stack) == 1:
        return stack.pop()
    else:
        print "Wrong elements"

def print_tree(tree, level):
    if tree == None: return
    print ' ' * level + str(tree.data)
    print_tree(tree.left, level + 1)
    print_tree(tree.right, level + 1)


res = get_tree("26*38/+65*%12-$")
print_tree(res, 0)

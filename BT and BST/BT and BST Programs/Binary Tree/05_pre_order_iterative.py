class BTNode:
    """Binary Tree Node"""
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class StackNode:
    """Stack Node for Linked List-based Stack"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Stack implementation using a linked list"""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        temp = StackNode(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            return None
        ptr = self.top.data
        self.top = self.top.next
        return ptr


def pre_order_iterative(root):
    if not root:
        return

    stack = Stack()
    stack.push(root)

    while not stack.is_empty():
        current = stack.pop()
        print(current.item, end=" ")
        # right first so left comes off the stack next (LIFO)
        if current.right:
            stack.push(current.right)
        if current.left:
            stack.push(current.left)


if __name__ == "__main__":
    # Creating a sample Binary Tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = BTNode(1)
    root.left = BTNode(2)
    root.right = BTNode(3)
    root.left.left = BTNode(4)
    root.left.right = BTNode(5)

    print("Pre-Order Traversal (stack):")
    pre_order_iterative(root)

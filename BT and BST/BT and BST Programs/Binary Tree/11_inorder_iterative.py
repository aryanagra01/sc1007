class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
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


def inorder_iterative(root):
    stack = Stack()
    current = root

    while current or not stack.is_empty():
        while current:
            stack.push(current)
            current = current.left
        current = stack.pop()
        print(current.data, end=" ")
        current = current.right


if __name__ == "__main__":
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("In-Order Traversal (stack):")
    inorder_iterative(root)

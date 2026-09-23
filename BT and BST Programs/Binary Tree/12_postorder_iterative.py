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


def postorder_iterative(root):
    if not root:
        return

    s1 = Stack()
    s2 = Stack()
    s1.push(root)

    while not s1.is_empty():
        current = s1.pop()
        s2.push(current)
        if current.left:
            s1.push(current.left)
        if current.right:
            s1.push(current.right)

    while not s2.is_empty():
        current = s2.pop()
        print(current.data, end=" ")


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

    print("Post-Order Traversal (two stacks):")
    postorder_iterative(root)

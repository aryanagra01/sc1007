class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth(node):
    if node is None:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


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

    print("Maximum depth:", max_depth(root))

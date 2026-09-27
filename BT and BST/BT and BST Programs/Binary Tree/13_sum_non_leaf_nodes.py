class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_non_leaf_nodes(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 0
    return node.data + sum_non_leaf_nodes(node.left) + sum_non_leaf_nodes(node.right)


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

    print("Sum of non-leaf nodes:", sum_non_leaf_nodes(root))

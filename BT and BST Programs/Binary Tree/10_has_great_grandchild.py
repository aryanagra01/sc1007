class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.data))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")


def has_great_grandchild(node):
    if node is None:
        return -1

    left_h = has_great_grandchild(node.left)
    right_h = has_great_grandchild(node.right)

    if max(left_h, right_h) > 1:
        print(node.data, end=" ")

    return 1 + max(left_h, right_h)


if __name__ == "__main__":
    #            1
    #           / \
    #          2   3
    #         /     \
    #        4       7
    #       /         \
    #      8          15
    #     /             \
    #   16              31

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.left.left = Node(8)
    root.left.left.left.left = Node(16)
    root.right = Node(3)
    root.right.right = Node(7)
    root.right.right.right = Node(15)
    root.right.right.right.right = Node(31)

    print("Tree Structure:")
    printTree(root)
    print("\nNodes with great-grandchildren:", end=" ")
    has_great_grandchild(root)
    print()

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_min(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node


def find_max(node):
    if node is None:
        return None
    while node.right is not None:
        node = node.right
    return node


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)


def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.data))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")


if __name__ == "__main__":
    #          10
    #         /  \
    #        5    15
    #       / \   / \
    #      2   7 12 18

    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.left = Node(12)
    root.right.right = Node(18)

    print("BST structure:")
    printTree(root)

    print("\nIn-order (sorted):")
    inorder(root)

    print("\n\nMin:", find_min(root).data)
    print("Max:", find_max(root).data)

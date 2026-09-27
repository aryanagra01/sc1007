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


def mirror_tree(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    mirror_tree(node.left)
    mirror_tree(node.right)


if __name__ == "__main__":
    #        4
    #       / \
    #      5   2
    #       \ / \
    #       6 3  1

    root = Node(4)
    root.left = Node(5)
    root.right = Node(2)
    root.left.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(1)

    print("Original Tree Structure:")
    printTree(root)

    mirror_tree(root)

    print("\nMirrored Tree Structure:")
    printTree(root)

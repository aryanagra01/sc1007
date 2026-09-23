class BTNode:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

def print_tree_in_order(node):
    if node is None:
        return
    print_tree_in_order(node.left)
    print(node.item, end=", ")
    print_tree_in_order(node.right)

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.item))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def mirrorTree(node):
# Write your code here #

#likely reievely swap the bottom and then swap upwards until you hit the node
    
    #base case
    if node is None:
        return

    #swapping mechanism
    else:
        #mirror below first
        mirrorTree(node.left)
        mirrorTree(node.right)

        #then swap
        temp = node.left
        node.left = node.right
        node.right = temp

if __name__ == "__main__":
    root = BTNode(4)
    root.left = BTNode(5)
    root.right = BTNode(2)
    root.left.left = None
    root.left.right = BTNode(6)
    root.right.left = BTNode(3)
    root.right.right = BTNode(1)

    print("Original Tree Structure:")
    printTree(root)
    print("\nOriginal Tree (In-Order):")
    print_tree_in_order(root)
    print()

    mirrorTree(root)
    
    print("\nMirrored Tree Structure:")
    printTree(root)
    print("\nMirrored Tree (In-Order):")
    print_tree_in_order(root)
    print()
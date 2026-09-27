from getopt import gnu_getopt


class Node:
    """Represents a node in the Binary Search Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    
    if data < node.data:
        if node.left is None:
            node.left = Node(data)
            return
        insert(node.left, data)
    elif data > node.data:
        if node.right is None:
            node.right = Node(data)
            return
        insert(node.right, data)
    else:
        return

def printTree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * level + prefix + str(node.data))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

def inorder_traversal(node):
    """Performs in-order traversal (Left, Root, Right)."""
    if node:
        inorder_traversal(node.left)
        print(node.data, end=" ")
        inorder_traversal(node.right)

# Example Usage
if __name__ == "__main__":
    # Create initial root node
    root = Node(10)
    
    # Insert nodes
    insert(5, root)
    insert(15, root)
    insert(2, root)
    insert(7, root)
    insert(12, root)
    insert(18, root)
    
    # Print the tree using inorder traversal
    print("In-Order Traversal of BST:")
    inorder_traversal(root)
    print("")
    print("\nFinal BST structure:")
    printTree(root)
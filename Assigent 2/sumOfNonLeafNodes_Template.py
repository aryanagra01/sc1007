class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    """ Inserts a node into the BST. """
    if root is None:
        return BSTNode(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
        
    return root

def inorderRecursive(root):
    """ Prints in-order traversal of the BST (Left, Root, Right). """
    if root:
        inorderRecursive(root.left)
        print(root.data, end=" ")
        inorderRecursive(root.right)


def sumOfNonLeafNodes(root):
# Write your code here #
    if root is None:
        return 0
    
    #lead dont add up
    if root.right is None and root.left is None:
        return 0

    return root.data + sumOfNonLeafNodes(root.right) + sumOfNonLeafNodes(root.left)

if __name__ == "__main__":
    root = None
    print("1: Insert an integer into BST")
    print("2: Sum of all non-leaf nodes")
    print("0: Quit")
    
    while True:
        choice = int(input("\nPlease input your choice (1/2/0): "))
        
        if choice == 1:
            value = int(input("Input an integer to insert: "))
            root = insert(root, value)
            # Automatically print in-order traversal after each insertion
            print("In-order traversal: ", end="")
            inorderRecursive(root)
            print()
        elif choice == 2:
            print(f"Sum of non-leaf nodes: {sumOfNonLeafNodes(root)}")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")
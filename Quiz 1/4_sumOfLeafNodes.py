"""
4. sumOfLeafNodes

Given a Binary Search Tree (BST), implement a function to find and return
the sum of all leaf nodes. A leaf node is any node that has no children.

Constraints:
- The BST is non-empty.
- The BST follows the standard binary search tree property:
  the left subtree contains only nodes with values less than the root,
  and the right subtree contains only nodes with values greater than the root.
- The function must use recursion to compute the sum.

Function prototype:
    def sumOfLeafNodes(root):

Input format:
1. The BST is built from user input.
2. The user enters multiple integers, and each integer is inserted into the BST.
3. The function sumOfLeafNodes(root) is called to compute the sum.

Output format:
    An integer representing the sum of all leaf nodes.

Example 1:
            10
           /  \\
          5    20
         / \\     \\
        3   7     30
    Sum of leaf nodes: 3 + 7 + 30 = 40

Example 2:
            15
           /  \\
         10    25
        /  \\     \\
       5    12    30
    Sum of leaf nodes: 5 + 12 + 30 = 47

Score: 100/100
"""


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    """Inserts a node into the BST."""
    if root is None:
        return BSTNode(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorderRecursive(root):
    """Prints in-order traversal of the BST (Left, Root, Right)."""
    if root:
        inorderRecursive(root.left)
        print(root.data, end=" ")
        inorderRecursive(root.right)


def sumOfLeafNodes(root):
    # Write your code here #
    # mo need check for empty
    # must use recusion
    if root is None:
        return 0
    if root.left or root.right:
        return sumOfLeafNodes(root.left) + sumOfLeafNodes(root.right)
    else:
        return root.data


if __name__ == "__main__":
    root = None
    print("1: Insert an integer into BST")
    print("2: Sum of all leaf nodes")
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
            print(f"Sum of leaf nodes: {sumOfLeafNodes(root)}")
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

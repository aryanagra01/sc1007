# ============================================================================
# Lab 4 – kthSmallest(root, k)
# ============================================================================
# DESCRIPTION
# Given the root of a Binary Search Tree (BST) and an integer k, return the
# k-th smallest value in the tree (1-indexed). Because it is a BST, an
# in-order traversal visits the nodes in ascending order, so the k-th node
# visited is the answer.
#
# Your solution should use O(h) extra space, where h is the height of the tree.
#
# INPUT
# root (BTNode) — the root of a BST with distinct values
# k (int) — which smallest value to return, 1-indexed
#
# In the test cases the tree is written as the list of values in the order
# they were inserted with insertBSTNode. For example, given
# root = [20, 8, 22, 4, 12, 10, 14], k = 3:
#   Inserting those values gives root 20, with 8 and 22 as its children,
#   4 and 12 under 8, and 10 and 14 under 12.
#   In-order traversal: 4, 8, 10, 12, 14, 20, 22
#
# OUTPUT
# A single integer — the k-th smallest value in the tree.
# Return -1 if k is less than 1 or greater than the number of nodes.
# For the example above: 10
#
# TASK
# Complete kthSmallest and return the k-th smallest value as an integer,
# using O(h) extra space where h is the height of the tree.
# ============================================================================

class BTNode:
    def __init__(self, data, left=None, right=None):
        self.data = data    # the value stored in this node (an integer)
        self.left = left    # reference to the left child node, or None
        self.right = right  # reference to the right child node, or None

def insertBSTNode(root, value):
    """ Recursive approach to insert a node into a BST (duplicates are ignored). """
    if root is None:
        return BTNode(value)
    if value < root.data:
        root.left = insertBSTNode(root.left, value)
    elif value > root.data:
        root.right = insertBSTNode(root.right, value)
    return root

def findMin(node):
    """ Find the node with the smallest value in a subtree (the left-most node). """
    while node.left is not None:
        node = node.left
    return node

def printBSTInOrder(node):
    """ Print BST items in sorted order using in-order traversal. """
    if node:
        printBSTInOrder(node.left)
        print(node.data, end=" ")
        printBSTInOrder(node.right)

def printTree(node, level=0, prefix="Root: "):
    """ Pretty prints the tree structure for better visualization """
    if node is not None:
        print(" " * level + prefix + str(node.data))
        if node.left or node.right:
            if node.left:
                printTree(node.left, level + 4, "L--- ")
            if node.right:
                printTree(node.right, level + 4, "R--- ")

class Solution:
    def kthSmallest(self, root, k):
        # -------- DO NOT MODIFY ANYTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------
        # Write your code here #
        if k < 1:
            return -1

        stack = []
        current = root

        while current or stack:
            while current: 
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1
            if k == 0:
                return current.data
            
            if current.right:
                current = current.right
            else:
                current = None
        
        return -1
            


        # -------- DO NOT MODIFY ANYTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------

if __name__ == "__main__":
    root = None
    print("BST Kth Smallest Element Program")
    print("=====================================")
    print("\nFirst, let's build the BST:")
    while True:
        try:
            value = input("\nEnter a value to insert (-1 to quit): ")
            if not value:
                continue
            i = int(value)
            if i == -1:
                break
            root = insertBSTNode(root, i)
            print("\nCurrent BST structure:")
            printTree(root)
            print("\nIn-order traversal: ", end="")
            printBSTInOrder(root)
            print()
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("\nNow let's find the k-th smallest element:")
    while True:
        try:
            k = input("\nEnter k (-1 to quit): ")
            if not k:
                continue
            k = int(k)
            if k == -1:
                break
            result = Solution().kthSmallest(root, k)
            if result != -1:
                print(f"\nThe {k}-th smallest element is: {result}")
            else:
                print("k is out of range for this tree!")
        except ValueError:
            print("Invalid input! Please enter an integer.")

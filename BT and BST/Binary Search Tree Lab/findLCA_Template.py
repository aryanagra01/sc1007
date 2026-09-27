# ============================================================================
# Lab 4 – findLCA(root, p, q)
# ============================================================================
# DESCRIPTION
# Given the root of a Binary Search Tree (BST) and two values p and q that
# are both in the tree, find their lowest common ancestor (LCA): the lowest
# node in the tree that has both p and q as descendants, where a node is
# allowed to be a descendant of itself.
#
# Use the BST property to decide which way to walk: if both values are
# smaller than the current node, the LCA lies in its left subtree; if both
# are larger, it lies in its right subtree; otherwise the current node is
# the LCA.
#
# INPUT
# root (BTNode) — the root of a BST with distinct values
# p (int) — the value of the first node
# q (int) — the value of the second node
#
# In the test cases the tree is written as the list of values in the order
# they were inserted with insertBSTNode. For example, given
# root = [6, 2, 8, 0, 4, 7, 9, 3, 5], p = 2, q = 8:
#   6 is the root, with 2 and 8 as its children
#   2 < 6 and 8 > 6, so the two values lie on different sides of 6
#
# OUTPUT
# A single integer — the value stored in the LCA node.
# For the example above: 6
# The node 6 is the lowest node with both 2 and 8 beneath it.
# If instead p = 2 and q = 4, the answer would be 2, since a node counts
# as its own ancestor.
#
# TASK
# Complete findLCA and return the value of the lowest common ancestor of
# the nodes p and q in the BST.
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
    def findLCA(self, root, p, q):
        # -------- DO NOT MODIFY ANYTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------
        # Write your code here #
        if root is None:
            return -1

        if p > q:
            p, q = q, p

        if p < root.data and root.data < q:
            return root.data
        elif p < root.data and q < root.data:
            return self.findLCA(root.left, p, q)
        elif p > root.data and q > root.data:
            return self.findLCA(root.right, p, q)
        else:
            return root.data

    def findLCAKey(self, root, p, q):
        if root is None:
            return -1
        if p < root.data and q < root.data:
            return self.findLCAKey(root.left, p, q)
        if p > root.data and q > root.data:
            return self.findLCAKey(root.right, p, q)
        return root.data

        # -------- DO NOT MODIFY ANYTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------

if __name__ == "__main__":
    root = None
    print("BST Lowest Common Ancestor Program")
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

    print("\nNow let's find lowest common ancestors:")
    while True:
        try:
            p = input("\nEnter first node value p (-1 to quit): ")
            if not p:
                continue
            p = int(p)
            if p == -1:
                break
            q = input("Enter second node value q: ")
            if not q:
                continue
            q = int(q)
            result = Solution().findLCA(root, p, q)
            if result != -1:
                print(f"\nThe LCA of {p} and {q} is: {result}")
            else:
                print("One or both values not found in the tree!")
        except ValueError:
            print("Invalid input! Please enter an integer.")

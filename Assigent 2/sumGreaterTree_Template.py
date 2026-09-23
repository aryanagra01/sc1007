class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)

    def printBTNode(self,space,left):
        if self.root is None:
            return
        else:
            self._printBTNode(self.root,space,left)

    def _printBTNode(self, node, space, left):
        if node is not None:
            # Print preceding spaces/branches
            for i in range(space - 1):
                print("|\t", end="")

            # Determine and print branch connectors for left/right child
            if space > 0:
                if left == 1:
                    print("|---", end="")
                else:
                    print("|___", end="")

            # Print the current node's item
            print(node.data)

            # Increment space for next level
            space += 1

            # Recursively print the left and right subtrees
            self._printBTNode(node.left, space, 1)   # left child
            self._printBTNode(node.right, space, 0)  # right child
            
    def sumGreaterTree(self):
        if self.root is None:
            return
        else:
            sum = 0
            self._sumGreaterTree(self.root, sum)

    def _sumGreaterTree(self, node, sum):
    # Write your code here #

bt = BinaryTree()

values = input().split()
for i in values:
    bt.insert(int(i))

bt.printBTNode(0,0)
print()
bt.sumGreaterTree()
bt.printBTNode(0,0)
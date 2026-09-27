class BTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class StackNode:
    def __init__(self, btnode):
        self.btnode = btnode
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

def createBTNode(item):
    return BTNode(item)

def push(stk, node):
    temp = StackNode(node)
    if stk.top is None:
        stk.top = temp
        temp.next = None
    else:
        temp.next = stk.top
        stk.top = temp

def pop(stk):
    if stk.top is None:
        return None
    
    temp = stk.top.next
    ptr = stk.top.btnode
    stk.top = temp
    return ptr

def printTree(node):
    if node is None:
        return
    printTree(node.left)
    print(node.item, end=" ")
    printTree(node.right)

def createTree():
    stk = Stack()
    root = None

    print("Input an integer that you want to add to the binary tree. Any Alpha value will be treated as NULL.")
    try:
        item = input("Enter an integer value for the root: ")
        root = createBTNode(int(item))
        push(stk, root)
    except ValueError:
        return None

    while True:
        temp = pop(stk)
        if temp is None:
            break

        try:
            item = input(f"Enter an integer value for the Left child of {temp.item}: ")
            temp.left = createBTNode(int(item))
        except ValueError:
            temp.left = None

        try:
            item = input(f"Enter an integer value for the Right child of {temp.item}: ")
            temp.right = createBTNode(int(item))
        except ValueError:
            temp.right = None

        if temp.right is not None:
            push(stk, temp.right)
        if temp.left is not None:
            push(stk, temp.left)

    return root

def removeAll(node):
    if node is not None:
        removeAll(node.left)
        removeAll(node.right)
        node.left = None
        node.right = None

def maxDepth(node):
# Write your code here #
    if node is None:
        return -1
    else:
        return 1 + max(maxDepth(node.left), maxDepth(node.right))


def main():
    root = None
    
    print("1: Create a binary tree.")
    print("2: Find the maximum depth of the binary tree.")
    print("0: Quit;")

    while True:
        try:
            c = int(input("\nPlease input your choice(1/2/0): "))
            
            if c == 1:
                root = None  # Clear existing tree
                root = createTree()
                print("The resulting binary tree is: ", end="")
                printTree(root)
                print()
            
            elif c == 2:
                depth = maxDepth(root)
                print(f"The maximum depth of the binary tree is: {depth}")
                root = None
            
            elif c == 0:
                if root:
                    removeAll(root)
                break
            
            else:
                print("Choice unknown;")
                
        except ValueError:
            continue

if __name__ == "__main__":
    main()
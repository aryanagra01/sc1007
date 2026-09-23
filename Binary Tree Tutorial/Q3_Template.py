class BSTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

def insertBSTNode(node_ref, value):
    if node_ref[0] is None:
        node_ref[0] = BSTNode(value)
    else:
        if value < node_ref[0].item:
            if node_ref[0].left is None:
                node_ref[0].left = BSTNode(value)
            else:
                insertBSTNode([node_ref[0].left], value)
        elif value > node_ref[0].item:
            if node_ref[0].right is None:
                node_ref[0].right = BSTNode(value)
            else:
                insertBSTNode([node_ref[0].right], value)

def push(stack, node):
    temp = StackNode(node)
    
    if stack.top is None:
        stack.top = temp
        temp.next = None
    else:
        temp.next = stack.top
        stack.top = temp

def pop(s):
    if s.top is None:
        return None
        
    temp = s.top.next
    ptr = s.top.data
    s.top = temp
    return ptr

def peek(s):
    if s.top is None:
        return None
    return s.top.data

def isEmpty(s):
    return s.top is None

def removeAll(node_ref):
    if node_ref[0] is not None:
        removeAll([node_ref[0].left])
        removeAll([node_ref[0].right])
        node_ref[0] = None

def preOrderIterative(root):
# Write your code here #
    if root is None:
        return
    
    s = Stack()
    push(s, root)

    while not isEmpty(s):
        current = pop(s)
        print(current.item, end = " ")
        if current.right is not None:
            push(s, current.right)
        if current.left is not None:
            push(s, current.left)

def main():
    root = [None]  # Using list to simulate pointer reference
    
    print("1: Insert an integer into the binary search tree;")
    print("2: Print the pre-order traversal of the binary search tree;")
    print("0: Quit;")
    
    while True:
        try:
            c = int(input("Please input your choice(1/2/0): "))
            
            if c == 1:
                i = int(input("Input an integer that you want to insert into the Binary Search Tree: "))
                insertBSTNode(root, i)
            
            elif c == 2:
                print("The resulting pre-order traversal of the binary search tree is: ", end="")
                preOrderIterative(root[0])
                print()
            
            elif c == 0:
                removeAll(root)
                break
            
            else:
                print("Choice unknown;")
                
        except ValueError:
            print("Invalid input")
            continue

if __name__ == "__main__":
    main()
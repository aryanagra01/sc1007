class BSTNode:
   def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None

class StackNode:
   def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
   def __init__(self):
       self.top = None

def insert(root, data):
   if root is None:
       return BSTNode(data)
   
   if data < root.data:
       root.left = insert(root.left, data)
   else:
       root.right = insert(root.right, data)
       
   return root

def push(stack, node):
   temp = StackNode(node)
   if stack.top is None:
       stack.top = temp
       temp.next = None
   else:
       temp.next = stack.top
       stack.top = temp

def pop(stack):
   if stack.top is not None:
       temp = stack.top
       stack.top = temp.next
       return temp.data
   return None

def is_empty(stack):
   return stack.top is None

def postOrderIterativeS2(root):
    # Your idea: stackMid parks "me", stackRight parks my right child.
    # See each node twice: first go right, second print (left already done).
    stackMid = Stack()
    stackRight = Stack()

    if root is None:
        return

    current = root

    while current or not is_empty(stackMid):
        while current:
            push(stackMid, current)
            push(stackRight, current.right)  # None is fine; just don't treat it as "still waiting"
            current = current.left

        current = pop(stackMid)
        rightCheck = pop(stackRight)

        # First visit + real right child still on stackRight -> go right, park myself
        if current.right is not None and current.right == rightCheck:
            push(stackMid, current)
            current = current.right
        else:
            # Second visit: rightCheck belongs to a parent, put it back
            # Leaf / no right: rightCheck is None, so do not push None back
            if rightCheck is not None:
                push(stackRight, rightCheck)
            print(current.data, end=" ")
            current = None


def postOrderInterativeS2_correct (root):
    if root is None:
        return

    stack1 = Stack()
    stack2 = Stack()
    push(stack1, root)

    while not is_empty(stack1):
        current = pop(stack1)
        if current.left is not None:
            push(stack1, current.left)
        if current.right is not None:
            push(stack1, current.right) 
        push(stack2, current)
    
    while not is_empty(stack2):
        print(pop(stack2).data, end = " ")
    




if __name__ == "__main__":
   root = None
   choice = 1

   print("1: Insert an integer into the binary search tree")
   print("2: Print the post-order traversal of the binary search tree")
   print("0: Quit")

   while choice != 0:
       choice = int(input("\nPlease input your choice(1/2/0): "))
       
       if choice == 1:
           value = int(input("Input an integer to insert: "))
           root = insert(root, value)
       elif choice == 2:
           print("Post-order traversal: ", end="")
           postOrderIterativeS2(root)
           print()
       elif choice == 0:
           break
       else:
           print("Choice unknown")
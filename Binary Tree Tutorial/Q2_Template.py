class BSTNode:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.nextPtr = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

def insert_bst_node(node_ref, value):
    if node_ref[0] is None:
        node_ref[0] = BSTNode(value)
    else:
        if value < node_ref[0].item:
            if node_ref[0].left is None:
                node_ref[0].left = BSTNode(value)
            else:
                insert_bst_node([node_ref[0].left], value)
        elif value > node_ref[0].item:
            if node_ref[0].right is None:
                node_ref[0].right = BSTNode(value)
            else:
                insert_bst_node([node_ref[0].right], value)

def enqueue(queue, node):
    new_node = QueueNode(node)
    
    if is_empty(queue.head):
        queue.head = new_node
    else:
        queue.tail.nextPtr = new_node
    
    queue.tail = new_node

def dequeue(queue):
    if queue.head is not None:
        node = queue.head.data
        queue.head = queue.head.nextPtr
        if queue.head is None:  # If the queue becomes empty
            queue.tail = None
        return node
    return None

def is_empty(head):
    return head is None

def remove_all(node_ref):
    if node_ref[0] is not None:
        remove_all([node_ref[0].left])
        remove_all([node_ref[0].right])
        del node_ref[0]

def level_order_traversal(root):
 # Write your code here #
    #BFS using a queue starting at root node level
    #only enqqueuand dequeue
    #node sent

    if root is None:
        return

    q = Queue()
    enqueue(q, root)

    while not is_empty(q.head):
        current = dequeue(q)
        print(current.item, end = " ")
        if current.left is not None:
            enqueue(q, current.left)
        if current.right is not None:
            enqueue(q, current.right)

# Main function to run the program.
if __name__ == "__main__":
    c = 1
    root = [None]  # Use a list to allow modification of the root reference

    print("1: Insert an integer into the binary search tree;")
    print("2: Print the level-order traversal of the binary search tree;")
    print("0: Quit;")

    while c != 0:
        c = int(input("Please input your choice(1/2/0): "))

        if c == 1:
            i = int(input("Input an integer that you want to insert into the Binary Search Tree: "))
            insert_bst_node(root, i)
        
        elif c == 2:
            print("The resulting level-order traversal of the binary search tree is: ", end="")
            level_order_traversal(root[0])  # Pass the actual root node
            print()
        
        elif c == 0:
            remove_all(root)
        
        else:
            print("Choice unknown;")
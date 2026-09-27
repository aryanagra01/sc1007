class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Node:
    """Stack Node for Linked List-based Stack"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Stack implementation using a linked list"""
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        temp = Node(data)
        temp.next = self.top
        self.top = temp

    def pop(self):
        if self.is_empty():
            return None
        ptr = self.top.data
        self.top = self.top.next
        return ptr

class Queue:
    """Queue implementation using a linked list"""
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return dequeued_data

def preorder (node):
    if node:
        print(node.data, end = " ")
        preorder(node.left)
        preorder(node.right)
    else:
        return

def postorder (node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end = " ")
    return

def inorder (node):
    if node:
        inorder(node.left)
        print(node.data, end = " ")
        inorder(node.right)

def preorderWithStack(node):
    if not node:
        return
    
    s = Stack()
    s.push(node)

    while not s.is_empty():
        current = s.pop()
        print(current.data, end= " ")
        if current.right:
            s.push(current.right)
        if current.left:
            s.push(current.left)

def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def kth_level_descendants (node, k):
    if not node:
        return []

    elif k == 0:
        return [node.data]
    
    return kth_level_descendants(node.left, k-1) + kth_level_descendants(node.right, k-1)

def calc_heigth(node):
    if not node:
        return -1

    return 1 + max(calc_heigth(node.left), calc_heigth(node.right))

def BFS (node):
    if not node:
        return
    
    q = Queue()
    q.enqueue(node)

    while not q.is_empty():
        current = q.dequeue()
        print (current.data, end = " ")
        if current.left:
            q.enqueue(current.left)
        if current.right:
            q.enqueue(current.right)







class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0  
       
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")
            
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
   
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
           
        new_node = Node(data)
       
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
       
        prev_node = self.findNode(index - 1)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def removeNode(self, index):
        if self.head is None:
            raise ValueError("List is empty")
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
            
        pre = self.findNode(index - 1)
        if pre.next is not None:
            pre.next = pre.next.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end="  ")
            cur = cur.next
        print("")

class Stack:
    def __init__(self):
        self.ll = LinkedList()
       
    def push(self, data):    
        try:
            self.ll.insertNode(data, 0)
        except ValueError as e:
            print(e)
       
    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        try:
            self.ll.removeNode(0)
        except ValueError as e:
            print(e)
            return None
        return data
       
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data    
       
    def isEmpty(self):
        return self.ll.size == 0
   
    def getSize(self):
        return self.ll.size
       
    def printStack(self):
        self.ll.printList()

def deleteMiddleElement(s):
# write your code here #
    temp = Stack()

    if s.isEmpty():
        return
    
    depth = (s.getSize() // 2)
    for _ in range(depth):
        mover = s.pop()
        temp.push(mover)
    
    s.pop()

    while not temp.isEmpty():
        mover = temp.pop()
        s.push(mover)
    
    return s
    

if __name__ == "__main__":
    s = Stack()
   
    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()
   
    counter = 0
    for num in numbers:
        try:
            s.push(int(num))
        except ValueError:
            break
   
    print("\nBefore:", end=" ")
    s.printStack()
   
    deleteMiddleElement(s)
   
    print("After:", end=" ")
    s.printStack()
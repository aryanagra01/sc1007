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
            return None
        if self.head is None:
            return None
           
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
   
    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            return None
           
        new_node = Node(data)
       
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
       
        prev_node = self.findNode(index - 1)
        if prev_node is None:
            return None
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return True

    def removeNode(self, index):
        if self.head is None:
            return None
        if index < 0 or index >= self.size:
            return None
           
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True
           
        pre = self.findNode(index - 1)
        if pre is None or pre.next is None:
            return None
        pre.next = pre.next.next
        self.size -= 1
        return True
       
    def print_list(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print("")
       
    def remove_all_items(self):
        self.head = None
        self.size = 0

class Stack:
    def __init__(self):
        self.ll = LinkedList()
       
    def push(self, data):    
        return self.ll.insertNode(data, 0)
       
    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        if self.ll.removeNode(0):
            return data
        return None
       
    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data    
       
    def isEmpty(self):
        return self.ll.size == 0

class Queue:
    def __init__(self):
        self.ll = LinkedList()
       
    def enqueue(self, data):    
        return self.ll.insertNode(data, self.ll.size)
       
    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data    
        if self.ll.removeNode(0):
            return data
        return None

    def isEmpty(self):
        return self.ll.size == 0

def reverse_stack(stack):
# Write your code here #
    if stack.isEmpty():
        return

    q = Queue()
    while not stack.isEmpty():
        trasnfer = stack.pop()
        q.enqueue(trasnfer)
    
    while not q.isEmpty():
        trasnfer02 = q.dequeue()
        stack.push(trasnfer02)
    
    return

# Main function
def main():
    s = Stack()
    while True:
        print("1: Insert an integer into the stack;")
        print("2: Reverse the stack;")
        print("0: Quit;")

        choice = int(input("Please input your choice(1/2/0): "))
        if choice == 1:
            value = int(input("Input an integer that you want to insert into the stack: "))
            s.push(value)
            print("The resulting stack is: ", end="")
            s.ll.print_list()
        elif choice == 2:
            reverse_stack(s)
            print("The resulting stack after reversing its elements is: ", end="")
            s.ll.print_list()
            s.ll.remove_all_items()
        elif choice == 0:
            s.ll.remove_all_items()
            break
        else:
            print("Choice unknown.")

if __name__ == "__main__":
    main()
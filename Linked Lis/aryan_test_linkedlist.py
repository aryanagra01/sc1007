class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

class LinkedList:
    def __init__(self):
       self.head = None
       self.size = 0

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def findNode (self, index):
        if self.head is None or index < 0 or index >= self.size:
            return None

        # start traversing from the head
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insert(self, data, index):
        if index < 0 or index > self.size:
            print("Index out of range")
            return False
    
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True
        
        else:   
            prev_node = self.findNode(index - 1)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True

    def removeNode(self, index):
        if index < 0 or index > self.size:
            print("Index out of range")
            return False 
        
        


        

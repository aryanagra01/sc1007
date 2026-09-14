
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
       
    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end="  ")
            cur = cur.next
        print("")
       
    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
       
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur
       
    def insertNode(self, index, data):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")
           
        new_node = Node(data)
       
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
           
        else:
            prev_node = self.findNode(index - 1)
            new_node.prev = prev_node
            new_node.next = prev_node.next
            if prev_node.next:
                prev_node.next.prev = new_node
            prev_node.next = new_node
       
        self.size += 1
       
    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
            
        if self.head is None:
            raise ValueError("List is empty")
           
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return True
           
        current = self.findNode(index)
        current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        self.size -= 1
        return True

def reverseDoublyList(head):

    if head is None or head.next is None:
        return head

    cur = head
    prev = None

    while cur:
        next = cur.next
        cur.prev = next
        cur.next = prev
        prev = cur
        cur = next
    
    head = prev
    return head


if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
   
    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()
   
    counter = 0
    for num in numbers:
        try:
            doubly_linked_list.insertNode(counter, int(num))
            counter += 1
        except ValueError:
            break
   
    print("\nBefore:", end=" ")
    doubly_linked_list.printList()
   
    doubly_linked_list.head = reverseDoublyList(doubly_linked_list.head)
    print("After:", end=" ")
    doubly_linked_list.printList()
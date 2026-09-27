class ListNode:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
 
    def print_list(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return 0
        prev_node = self.find_node(index - 1)
        if prev_node is None:
            return -1
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
        return 0

    def remove_node(self, index):
        if self.head is None:
            return -1
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return 0
        prev_node = self.find_node(index - 1)
        if prev_node is None or prev_node.next is None:
            return -1
        prev_node.next = prev_node.next.next
        self.size -= 1
        return 0

    def remove_all_items(self):
        self.head = None
        self.size = 0

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        self.ll.insert_node(0, item)

    def pop(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.head.item

    def is_empty(self):
        return self.ll.size == 0

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, item):
        self.ll.insert_node(self.ll.size, item)

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.ll.head.item
        self.ll.remove_node(0)
        return item

    def is_empty(self):
        return self.ll.size == 0

def reverse_first_k_items(queue, k):
# Write your code here #
    if queue.isEmmpty() or k <=0 or k > queue.ll.size:
        return
    
    stack = Stack()
    for _ in range(k):
        stack.push(queue.dequeue())

    while not stack.isEmpty():
        queue.enqueue(stack.pop())
    
    for _ in range(queue.ll.size - k):
        queue.enqueue(queue.dequeue())


def main():
    q = Queue()
    while True:
        print("1: Insert an integer into the queue;")
        print("2: Reverse the elements of the queue until the given number;")
        print("0: Quit;")
        choice = int(input("Please input your choice(1/2/0): "))
        if choice == 1:
            value = int(input("Input an integer that you want to insert into the queue: "))
            q.enqueue(value)
            print("The resulting queue is: ", end="")
            q.ll.print_list()
        elif choice == 2:
            value = int(input("Enter an integer to reverse the queue until that number: "))
            reverse_first_k_items(q, value)
            print(f"The resulting queue after reversing first {value} elements is: ", end="")
            q.ll.print_list()
            q.ll.remove_all_items()
        elif choice == 0:
            q.ll.remove_all_items()
            break
        else:
            print("Choice unknown;")

if __name__ == "__main__":
    main()
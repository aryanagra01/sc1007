class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front= None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeu from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node

    def getFront(self):
        if self.isEmpty():
            raise IndexError("Peak from empty queue")
        return self.front.data

    def getSize(self):
        return self.size

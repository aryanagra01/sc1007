"""
1. reverseQueueSegment

Given a queue and two indices, m and n, reverse the portion of the queue
from index m to index n (inclusive) while keeping the rest unchanged.

Constraints:
- The queue is non-empty.
- The reversal must be performed using only one temporary stack.
- You only use standard queue operations (enqueue, dequeue) and stack
  operations (push, pop).
- No additional data structures (such as lists or arrays) can be used.

Function prototype:
    def reverseQueueSegment(queue, m, n):

Parameters:
    queue: A queue containing integers.
    m: The starting index of the segment to be reversed.
    n: The ending index of the segment to be reversed.
Returns: The modified queue.

Input format:
1. A space-separated list of integers representing the queue.
2. Two integers m and n where 0 <= m <= n < (length of the queue).

Example 01:
    Original Queue: 10 20 30 40 50 60 70
    m = 2, n = 5
    Modified Queue: 10 20 60 50 40 30 70

Example 02:
    Original Queue: 1 2 3 4 5 6
    m = 1, n = 3
    Modified Queue: 1 4 3 2 5 6

Score: 100/100
"""


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def find_node(self, index):
        if index < 0 or index >= self.size:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def remove_node(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.find_node(index - 1)
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
        return 0

    def insert_node(self, index, value):
        if index < 0 or index > self.size:
            return -1
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.find_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1
        return 0

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print(" ")


class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, data):
        self.ll.insert_node(0, data)

    def pop(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data
        self.ll.remove_node(0)
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.ll.head.data

    def isEmpty(self):
        return self.ll.size == 0

    def get_size(self):
        return self.ll.size


class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, data):
        self.ll.insert_node(self.ll.size, data)

    def dequeue(self):
        if self.isEmpty():
            return None
        data = self.ll.head.data
        self.ll.remove_node(0)
        return data

    def getFront(self):
        if self.isEmpty():
            raise IndexError("Peek from empty queue")
        return self.ll.head.data

    def getSize(self):
        return self.ll.size

    def isEmpty(self):
        return self.ll.size == 0

    def printQueue(self):
        self.ll.printList()


def reverseQueueSegment(queue, m, n):
    # Write your code here #

    # index m to n inclusive
    # non empty so dont need check, unless m and n fall out of size, also dont need because main checks already
    # only 1 temporary stack
    # no list or arrays
    # start at 0 and end at size-1

    # likely dequaeue and enqueu so not reversed
    # reversed the indexes using the stack

    size = queue.getSize()
    stack = Stack()

    for _ in range(m):
        queue.enqueue(queue.dequeue())

    for _ in range(n - m + 1):
        stack.push(queue.dequeue())

    while not stack.isEmpty():
        queue.enqueue(stack.pop())

    for _ in range(size - n - 1):
        queue.enqueue(queue.dequeue())


if __name__ == "__main__":
    queue = Queue()

    print("Enter a list of numbers, terminated by any non-digit character: ", end="")
    input_string = input()
    numbers = input_string.split()

    for num in numbers:
        try:
            queue.enqueue(int(num))
        except ValueError:
            break

    m, n = map(int, input("Enter indices m and n separated by space: ").split())

    print("Original Queue:", end=" ")
    queue.printQueue()

    # Validate input indices before calling the function
    if m < 0 or n >= queue.getSize() or m > n:
        print("Invalid indices")
    else:
        reverseQueueSegment(queue, m, n)
        print("Modified Queue:", end=" ")
        queue.printQueue()


PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 3}

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        self.top = self.top.next
        self.size -= 1

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data

def in2preS(expr):
# Write your code here #
    operators = Stack()
    output = Stack()

    for char in expr[::-1]:

        if char.isalnum():
            output.push(char)
        
        elif char == ")":
            operators.push(char)
        elif char == "(":
            while not operators.isEmpty() and operators.peek() != ")":
                output.push(operators.peek())
                operators.pop()
            if not operators.isEmpty() and operators.peek() == ")":
                operators.pop()
        elif char in PRECEDENCE:

            while (not operators.isEmpty() and 
            operators.peek() != ")" and
            (PRECEDENCE[operators.peek()] > PRECEDENCE[char] or
            (PRECEDENCE[operators.peek()] == PRECEDENCE[char] and char == "**"))):
                output.push(operators.peek())
                operators.pop()
            operators.push(char)
        

    while not operators.isEmpty():
        output.push(operators.peek())
        operators.pop()

    return output





if __name__ == "__main__":
    infix = input("Enter infix expression: ")
    prefix = in2preS(list(infix.split(' ')))
    
    # Print the prefix expression
    result = ""
    while not prefix.isEmpty():
        result += prefix.peek()
        prefix.pop()
    
    print(f"Prefix expression: {result}")
"""
2. in2postS

Write a function, in2postS(), to convert an infix expression into a postfix
expression stack. The character string only contains positive integer numbers,
operators ('**', '+', '-', '*' and '/') and parentheses.

Function prototype:
    def in2postS(expr):

Example 01:
    Sample Input:  3 + 4 * 5
    Sample Output: 3 4 5 * +

Example 02:
    Sample Input:  ( 1 + ( 2 ** 3 ) * ( 4 / ( 5 - 6 ) ) )
    Sample Output: 1 2 3 ** 4 5 6 - / * +

Example 03:
    Sample Input:  ( ( 2 + 3 ) * ( 4 - 1 ) ) / ( 5 + ( 6 * ( 7 - 8 ) ) )
    Sample Output: 2 3 + 4 1 - * 5 6 7 8 - * + /

Score: 100/100
"""

# Define operator precedence globally
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

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return value

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.top.data


def in2postS(expr):
    # Write your code here #
    output = Stack()
    operator = Stack()

    for i in expr:
        if i == '(':
            operator.push(i)
        elif i == ')':
            while not operator.isEmpty() and operator.peek() != '(':
                output.push(operator.pop())
            if not operator.isEmpty() and operator.peek() == '(':
                operator.pop()
        elif i.isalnum():
            output.push(i)
        else:
            while (not operator.isEmpty() and operator.peek() != '(' and (PRECEDENCE[i] <= PRECEDENCE[operator.peek()]
            or (PRECEDENCE[i] == PRECEDENCE[operator.peek()] and i != '**'))):
                output.push(operator.pop())
            operator.push(i)

    while not operator.isEmpty():
        if operator.peek() == '(':
            operator.pop()
        else:
            output.push(operator.pop())

    return output


if __name__ == "__main__":
    infix = input("Enter infix expression (space separated): ")
    postfix = in2postS(list(infix.split(' ')))

    # Reverse stack to print in correct postfix order
    temp = Stack()
    while not postfix.isEmpty():
        temp.push(postfix.pop())

    result = ""
    while not temp.isEmpty():
        result += temp.pop() + " "

    print("Postfix expression:", result.strip())

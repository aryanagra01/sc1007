# Define operator precedence globally
PRECEDENCE = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

class Node:
    """Defines a node for a linked list-based stack"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Implements a stack using a linked list"""
    def __init__(self):
        self.top = None
        self.size = 0
       
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
       
    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        self.size -= 1
        return popped
       
    def peek(self):
        return None if self.is_empty() else self.top.data
       
    def is_empty(self):
        return self.size == 0

def has_higher_precedence(op1, op2):
    """Check if op1 has higher or equal precedence to op2"""
    if op1 not in PRECEDENCE or op2 not in PRECEDENCE:
        return False
    return PRECEDENCE[op1] >= PRECEDENCE[op2]

def infix_to_postfix(expression):
    output = ""
    operator_stack = Stack()
   
    i = 0
    while i < len(expression):
        #reading left to right
        char = expression[i]
       
        # Handle multi-digit numbers # need to use as a single number
        if char.isdigit():
            number = ""
            while i < len(expression) and expression[i].isdigit():
                number += expression[i]
                i += 1
            
            #put it straight into the ouput string, is output was stack then just straight push if number
            output += number + " "
            i -= 1  

        #if bracket opening push into the operator stack    
        elif char == '(':
            operator_stack.push(char)

        #if bracket closing need to empty out
        elif char == ')':

            #empty out until the opening bracket is hit by pushing into string
            while not operator_stack.is_empty() and operator_stack.peek() != '(':
                output += operator_stack.pop() + " "
           
            #once wall is hit, just pop it as in post fix and prefix the brackets are not needed
            if not operator_stack.is_empty() and operator_stack.peek() == '(':
                operator_stack.pop()

        #finally the operators
        elif char in PRECEDENCE:  # Check if character is an operator

            #1. check is not empty before popping 
            #2. check if its a open bracket because we do not want to pop that, but stack the operator on top
            #3. precendence check, if stack top higher or equal precendece, then pop it
            #   else if the stack top is not higher, meaning the added one has higher, then add the new operator
            while (not operator_stack.is_empty() and
                   operator_stack.peek() != '(' and
                   has_higher_precedence(operator_stack.peek(), char)):
                

                output += operator_stack.pop() + " "
           
           #this is the adding of the new operator after the old was was popped or not
            operator_stack.push(char)

        # Skip spaces
        elif not char.isspace():
            # For variables (letters)
            output += char + " "
       
        i += 1
   #clear all the operators at the end
    while not operator_stack.is_empty():
        output += operator_stack.pop() + " "
   
    return output.strip()

# Test the function
if __name__ == "__main__":
    infix_exp = input("Enter an infix expression: ")
    try:
        postfix_exp = infix_to_postfix(infix_exp)
        print(f"Postfix expression: {postfix_exp}")
    except ValueError as e:
        print(f"Error: {e}")
"""
Tokenised expressions. Each item is already one token.
"12" is one token. "**" is one token. There is no index and no space token.

Return a list of tokens, except the two evaluate functions, which return a number.
"""

from inspect import stack
from nt import error
import operator
from _support import Stack, check

PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


def infix_to_postfix(expr):
    """Left to right. (** is right to left.)
    ["3", "+", "4", "*", "5"] -> ["3", "4", "5", "*", "+"]
    ["2", "**", "3", "**", "2"] -> ["2", "3", "2", "**", "**"]
    """
    raise NotImplementedError


def infix_to_prefix(expr):
    """Right to left. Output is already in prefix order.
    ["3", "+", "4", "*", "5"] -> ["+", "3", "*", "4", "5"]
    """

    output = stack
    oerator = stack

    for i in epr[::-1]:
        #prefix means reads backwards
        if i == ")":
            pass  # push into operator
        elif i == "(":
            pass



def eval_postfix(expr):
    """["3", "4", "5", "*", "+"] -> 23
    ["2", "3", "2", "**", "**"] -> 512
    """
    stack = STack()

    for i in expr:

        if i:
            pass


def eval_prefix(expr):
    """["+", "3", "*", "4", "5"] -> 23
    """
    for i in expr:
        if i.isdigit():
            stack.push()
        else:
            op1 = stack.push
            op2=stack.pop

            if i =="+"



def postfix_to_infix(expr):
    """["3", "4", "5", "*", "+"] -> "(3 + (4 * 5))"
    """
    
    output = Stack()

    for i in expr:

        if i in PRECENENCE or i.isalum():
            output.push(i)
        else:
            if output.size < 2:
                raise ValueError("Invalid postfix expression: not enough operands")
            
            op2 = output.pop()
            op1 = output.pop()
        
            infix_expr = "( " + op1 + " " + i + " " + op2 + " )"
            output.push(infix_expr)
        
    if stack.size != 1:
        raise ValueError("invlaid nonse")
            


def prefix_to_infix(expr):
    """Raw string, not a token list. Right to left, with an index.
    "+ 3 * 4 5" -> "(3 + (4 * 5))"
    "+ 12 * 3 4" -> "(12 + (3 * 4))"
    """
    stack = Stack()
    i = len(expr) - 1

    # right to left, so the shared step at the bottom is i - 1.
    # your notes say i + 1 because that walk goes left to right.
    while i >= 0:
        char = expr[i]

        if char.isspace():
            i -= 1
            continue

        # operand: not an operator, or a letter/digit
        if char not in PRECEDENCE or char.isalnum():
            if char.isdigit():
                number = ""
                while i >= 0 and expr[i].isdigit():
                    number = expr[i] + number
                    i -= 1
                # inner loop left i one past the number.
                # the bottom i - 1 would move again and skip a character, so step back.
                # left to right this is your notes' i - 1. here the direction is flipped, so i + 1.
                i += 1  # do the opposite here
                stack.push(number)
            else:
                stack.push(char)

        else:
            # operator. prefix pops op1 first, then op2
            if stack.size() < 2:
                raise ValueError("Invalid prefix expression")

            op1 = stack.pop()
            op2 = stack.pop()
            infix_expr = "(" + op1 + " " + char + " " + op2 + ")"
            stack.push(infix_expr)

        i -= 1

    # 4. one finished expression should be left
    if stack.size() != 1:
        raise ValueError("Invalid prefix expression")

    return stack.pop()




def postfix_to_prefix(expr):
    """Raw string, left to right.
    "3 4 5 * +" -> "+ 3 * 4 5"
    "3 12 4 * +" -> "+ 3 * 12 4"
    """
    stack = Stack()
    i = 0
    max = len(expr) - 1

    while i <= max:
        char = expr[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit():
            number = ""
            while i <= max and expr[i].isdigit():
                number += expr[i]
                i += 1
            # inner loop left i one past the number.
            # the bottom i + 1 would skip a character, so step back.
            i -= 1
            stack.push(number)
        else:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")

            # postfix: pop op2 first, then op1
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = char + " " + op1 + " " + op2
            stack.push(new_expr)

        i += 1

    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")

    return stack.pop()
        



def prefix_to_postfix(expr):
    """["+", "3", "*", "4", "5"] -> "3 4 5 * +" as one string, with spaces.
    """
    stack = Stack()

    for i in expr[::-1]:
        if i.isdigit():
            stack.push(i)
        else:
            if stack.size< 2:
                raise ValueError
            
            op1 = stack.pop()
            op2 = stack.pop()

            new_expr = op1 + " " + op2 + " " + i
            stack.push(new_expr)

    if stack.size() != 1:
        raise error


if __name__ == "__main__":
    simple = ["3", "+", "4", "*", "5"]
    power = ["2", "**", "3", "**", "2"]
    post = ["3", "4", "5", "*", "+"]
    pre = ["+", "3", "*", "4", "5"]

    check("infix to postfix", lambda: infix_to_postfix(simple), ["3", "4", "5", "*", "+"])
    check("infix to postfix **", lambda: infix_to_postfix(power), ["2", "3", "2", "**", "**"])
    check("infix to prefix", lambda: infix_to_prefix(simple), ["+", "3", "*", "4", "5"])
    check("eval postfix", lambda: eval_postfix(post), 23)
    check("eval postfix **", lambda: eval_postfix(["2", "3", "2", "**", "**"]), 512)
    check("eval prefix", lambda: eval_prefix(pre), 23)
    check("postfix to infix", lambda: postfix_to_infix(post), "(3 + (4 * 5))")
    check("prefix to infix", lambda: prefix_to_infix("+ 3 * 4 5"), "(3 + (4 * 5))")
    check("prefix to infix 12", lambda: prefix_to_infix("+ 12 * 3 4"), "(12 + (3 * 4))")
    check("postfix to prefix", lambda: postfix_to_prefix("3 4 5 * +"), "+ 3 * 4 5")
    check("postfix to prefix 12", lambda: postfix_to_prefix("3 12 4 * +"), "+ 3 * 12 4")
    check("prefix to postfix", lambda: prefix_to_postfix(pre), "3 4 5 * +")

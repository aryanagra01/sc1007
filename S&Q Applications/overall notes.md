goign from pre or post

    1. ignore white spaces
        a. if char.isspace() --> continue
    2. then is operand push to the stack
        a. if more than 1 digit number need to do the check isdigit thing from below 
        b. also the loop would need to be a while loop for i less than lenght of expr
    3. if operator
        a) check if stack size is less then 2 raise error
        b) have 2 variables op1 and op2
            1. op2 is popped first for post
            2. op1 is popped first for pre
        c) combine togther
            1. to infix --> "(" + op1 + operator + op2 + ")"
            2. to pre --> operator + op1 + op2
            3. to post --> op1 + op2 + operator
        d) push the combined to stack
    4. check if stack size at the end is 1

    Notes
        1. if post --> left to right
            a. pop order --> op2 then op1
        2. if pre --> right to left
            a. pop order --> op1 then op2

going from infix 

    1. create 2 stacks
    2. read the string 
        a. if want to make pre --> right to left (can reverse string)
        b. if want to make post --> left to right
        c. while loop for i less than lenght of expr ( define i=0 before)
        d. char = expr[i]
    3. if space
        a. ignore and i+1 and write continue
    4. if character or letter (is alum)
        a. if letter (isalpha)
            1. push the letter into output
        b. else number (if digit)
            2. create an empty string
            3. continue moving down the expr 
                a. check if position not exceed lenght
                b. still a digit
                c. append new digit to the string
                d. i+1 and keep going
            4. add the whole number of the output
                a. do i-1 since i was put one ahead for the last check
                b. for pre reverse the number when adding it
    5. elif open bracket
        a. ) for prefix
        b. ( for post
        c. push into operator stack
    6. elif close bracket
        a. while operator stack not empty and peek to see not open bracket
                a. pop and push the operators
        b. if operator stack not empty and peek is open bracket
                a. remove the bracket
    7. elif operator 
        a. 3 conditions for while to pop out to add to output
            1. operator stack not empty before popping
            2. check if its a open bracket because we do not want to pop that, but stack the operator on top
            3. precendence check, if stack top higher or equal precendece, then pop it
                a. else if the stack top is not higher, meaning the added one has higher, then add the new operator
        b. stack the operator on top
    8. do i+1 
    9. after all the char has gone through
        a. while operator stack not empty, push it to the output
    10. if prefix then reverse 
        a. only if output is string
        b. for 2 stack the output is already reversed


evaluting number (same as pre/post to infix kind of)
    1. create a new stack
    2. read left to right for post, right to left for pre
    3. if digit then push to stack
    4. else if operator
        a. can do the check for check < 2 is invlaid
        a. op2 is popped first for post
        b. op1 is popped first for pre
        c. have a bunch of if statemnts for the diff operators
            1. stack.push op1 +/- op2
    5. return stack.pop()
        a. can do check if stack is != 1
        
        

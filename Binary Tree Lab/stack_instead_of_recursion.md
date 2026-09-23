STACK INSTEAD OF RECURSION (Binary Trees)
=========================================
You struggle with this because recursion HIDES the stack.
Python is already using a stack when you recurse — you just don't see it.
Iterative = you hold that stack yourself.


THE ONE SENTENCE
----------------
Recursion:  "I'll come back to this later"  (Python remembers for you)
Stack:      "I'll come back to this later"  (you push it, then pop it later)

Same idea. Stack is LIFO = last in, first out.
Whatever you push last is the next thing you work on.


PYTHON LIST = YOUR STACK
------------------------
    stack.append(x)   =  push
    stack.pop()       =  pop (takes the TOP / last one)
    stack[-1]         =  peek (look at top without removing)

There is often NO Stack class. Just use a list.


THE SKELETON (memorise this)
----------------------------
This is the shape of almost every "visit every node, no recursion" function.

    if root is None:
        return []          # or 0 / None / whatever the empty answer is

    result = []
    stack = [root]         # start: only the root is waiting

    while stack:           # still got unfinished nodes?
        curr = stack.pop() # take one out — this is "I'm standing here now"

        # --- DO THE QUESTION'S JOB ON curr ---
        # print it, check grandchild, compare to m, track min, etc.

        # --- SCHEDULE THE CHILDREN (this REPLACES the recursive calls) ---
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)

    return result

Memory trick: "pop → do work → push kids"
That's the whole function. The question only changes the middle "do work" bit.


WHAT REPLACES WHAT
------------------
Recursive:

    def f(node):
        if node is None: return
        # do work on node
        f(node.left)     # ← this is "I'll do left later"
        f(node.right)    # ← this is "I'll do right later"

Iterative:

    # do work on curr
    stack.append(curr.left)    # same as f(node.left)
    stack.append(curr.right)   # same as f(node.right)

You never write f(something). You push something instead.
The while loop is what actually goes there later.


PUSH ORDER (this trips people)
------------------------------
Stack = last in first out. So:

    push LEFT then RIGHT  →  next pop is RIGHT
    push RIGHT then LEFT  →  next pop is LEFT

If the question does NOT care about order (has_grandchild, smallest, print smaller):
    push order does not matter. Either is fine.

If the question DOES care (preorder left-to-right):
    push RIGHT first, then LEFT, so LEFT comes off the stack next.


WALKTHROUGH — has_grandchild
----------------------------
Question: which nodes have a grandchild? (a child that itself has a child)

Recursive version thinks:
    1. look at ME — do I have a grandchild?
    2. then recurse left
    3. then recurse right

Iterative is the SAME 3 steps, just with a stack:

    stack = [root]

    while stack:
        curr = stack.pop()          # 1. stand on a node

        has = False
        if curr.left:
            if curr.left.left or curr.left.right:
                has = True          # my left child has a kid → I have grandchild
            stack.append(curr.left) # 2. do left later
        if curr.right:
            if curr.right.left or curr.right.right:
                has = True
            stack.append(curr.right)# 3. do right later

        if has:
            result.append(curr.val)

Notice: the grandchild CHECK is on curr (the "do work").
The appends are just "visit these nodes later" — they are NOT the check.
Easy to mix those two up. Checking curr vs scheduling kids are different jobs.


TINY EXAMPLE (so you can see the stack move)
--------------------------------------------
        5
       / \
      3   8
     / \
    1   4

start:     stack = [5]
pop 5:     3 has kids 1 and 4 → 5 HAS grandchild. push 3, push 8
           stack = [3, 8]
pop 8:     8 has no children with kids → skip. nothing to push
           stack = [3]
pop 3:     1 and 4 have no kids → 3 has NO grandchild. push 1, push 4
           stack = [1, 4]
pop 4:     leaf. skip
pop 1:     leaf. skip
done. result = [5]


SAME SKELETON, OTHER LABS
-------------------------
Once you have the skeleton, you only change the "do work" line.

printSmallerValues (print node if node.item < m):

    while stack:
        curr = stack.pop()
        if curr.item < m:          # <-- only this line is the question
            print(curr.item, end=" ")
        if curr.left:  stack.append(curr.left)
        if curr.right: stack.append(curr.right)

smallest_value (keep a running min):

    smallest = root.item
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.item < smallest:   # <-- only this is the question
            smallest = curr.item
        if curr.left:  stack.append(curr.left)
        if curr.right: stack.append(curr.right)
    return smallest

mirrorTree iterative is a bit different: the "do work" is SWAP left/right,
then still push the (now swapped) children so you can swap them too.

    while stack:
        curr = stack.pop()
        curr.left, curr.right = curr.right, curr.left   # swap
        if curr.left:  stack.append(curr.left)
        if curr.right: stack.append(curr.right)


HOW TO WRITE ONE FROM SCRATCH (exam method)
-------------------------------------------
Don't try to "translate recursion in your head". Write this in order:

1) empty tree? return the empty answer
2) result / answer variable
3) stack = [root]
4) while stack:
      curr = stack.pop()
      ???                         ← fill this with what you'd do ON ONE NODE
      if curr.left:  push left
      if curr.right: push right
5) return result

The ??? is just: "if I was standing on this one node, what do I check/print/save?"
That is the same as the non-recursive part of your recursive function.


TWO TYPES OF QUESTIONS (this is why some feel impossible)
---------------------------------------------------------
TYPE A — "I can decide using only THIS node"
    has grandchild?  look at curr.left.left etc. Don't need the kids to finish first.
    print if < m?    look at curr.item. Done.
    smallest?        look at curr.item. Done.
    preorder print?  print curr, then visit kids.

    → use the skeleton. Easy. This is 90% of lab iterative questions.

TYPE B — "I need the children's ANSWERS before I can finish myself"
    height / hasGreatGrandchild:  height(me) = 1 + max(height(left), height(right))
    postorder:                    left, THEN right, THEN me
    identical (if you insisted iterative): need both subtrees' True/False first

    Recursion is naturally good at Type B because the recursive call RETURNS
    before the current function continues.

    Stack version is messier: you must visit a node TWICE
        first time  → push kids, don't finish yet
        second time → kids are done, NOW compute my answer

    Exam survival:
      Type A → skeleton above
      Type B postorder → trick: do a "backwards preorder" then reverse
            (see postOrderIterativeS1 Solution 1)
      Type B height    → just recurse unless they BAN recursion
            hasGreatGrandchild lab wants recursion. Don't fight it.


POSTORDER TRICK (Type B, but cheap)
-----------------------------------
Real postorder = left, right, root.

Cheat with one stack:
    do ROOT, RIGHT, LEFT  (push left then right so right pops first)
    then reverse the list
    → becomes LEFT, RIGHT, ROOT

    s = [root]
    while s:
        curr = s.pop()
        result.append(curr.val)     # record now (too early)
        if curr.left:  s.append(curr.left)
        if curr.right: s.append(curr.right)
    result.reverse()                # fix the order
    return result

That's Solution 1 in postOrderIterativeS1.
The hard one-stack "go left, peek if right is waiting, push myself back"
is Solution 2 — only learn it if the question FORBIDS reverse / 2nd list.


QUEUE VS STACK (don't mix them)
-------------------------------
Stack  (append + pop from END)     = DFS, same as recursion
Queue  (append + pop from FRONT)   = BFS, level by level

    from collections import deque
    q = deque([root])
    while q:
        curr = q.popleft()     # FRONT, not the end
        # do work
        if curr.left:  q.append(curr.left)
        if curr.right: q.append(curr.right)

If the question says "iterative + stack" → DFS skeleton.
If it says "level order" → queue, not stack.


COMMON MISTAKES
---------------
1) Forgetting to push children
   You check curr... then never append left/right → you only look at the root.

2) Pushing None
   Always `if curr.left:` before append. Popping None then doing curr.val crashes.

3) Thinking the stack IS the answer
   stack = "who still needs visiting"
   result = "the actual output"
   Don't confuse them.

4) Recursing AND using a stack
   If they said iterative, there should be NO f(node.left) call.

5) Using the stack for Type B like it's Type A
   hasGreatGrandchild needs height of kids FIRST.
   Peeking curr.left.left is Type A (grandchild).
   Height is Type B. Different question → different method.

6) Infinite loop
   You pop curr then accidentally push curr again (yourself), not the child.


WHICH TECHNIQUE WHEN?
---------------------
Visit every node, decide on the node itself?
    → stack skeleton (Type A). pop, do work, push kids.

has_grandchild / printSmaller / smallest / mirror?
    → Type A. Same skeleton, different "do work".

postorder, "one stack, no recursion"?
    → push kids + reverse trick (unless they ban reverse).

hasGreatGrandchild / height?
    → recurse. Need kids' return values. Don't force a stack.

level order / each level as a list?
    → queue (deque), not stack.

"Do I even need a stack?"
    Linked list walk? No. Just cur = cur.next.
    Tree? Yes if no recursion — a node has TWO nexts, so you must remember the other one.
    THAT is the real reason for the stack: a tree branches. You can't follow both
    children at once, so you park one on the stack.

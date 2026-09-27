STACK INSTEAD OF RECURSION
==========================
A tree node has two children. You can follow only one.
The other one has to wait.

Recursion: Python stores the waiting child on a hidden stack.
Iterative: you store it yourself.

    stack.append(x)   push
    stack.pop()       pop the last one you pushed
    stack[-1]         peek, leave it there

A Python list is the stack. There is often no Stack class.

This note is the loop for "look at this node, then visit both children".
The pre / in / post orders are in walking_notes.md.


THE LOOP
--------
Use this when the node you are standing on is enough.
You do not need a child to finish and return an answer first.

    if root is None:
        return []              # 0, None, or whatever the empty answer is

    result = []
    stack = [root]             # only the root is waiting

    while stack:
        curr = stack.pop()     # stand here
        # do the job on curr
        if curr.left:
            stack.append(curr.left)    # visit later
        if curr.right:
            stack.append(curr.right)

    return result

The question only changes the job on curr.
The pushes replace the two recursive calls.

    def f(node):
        # do the job on node
        f(node.left)
        f(node.right)

    # do the job on curr
    stack.append(curr.left)     # same as f(node.left)
    stack.append(curr.right)    # same as f(node.right)

Push order. The stack pops the last thing pushed.

    push left, then right   -> next pop is right
    push right, then left   -> next pop is left

If the question does not care about left-before-right, either order is fine.
Preorder left-to-right pushes right first, then left.


WHERE THIS LOOP IS USED
-----------------------
Has a grandchild. A grandchild is a child that itself has a child.
The check is on curr. The push only means visit that child later.

    while stack:
        curr = stack.pop()
        has = False
        if curr.left:
            if curr.left.left or curr.left.right:
                has = True
            stack.append(curr.left)
        if curr.right:
            if curr.right.left or curr.right.right:
                has = True
            stack.append(curr.right)
        if has:
            result.append(curr.val)

        5
       / \
      3   8
     / \
    1   4

    start     stack = [5]
    pop 5     3 has children, so 5 counts. push 3, push 8.  stack = [3, 8]
    pop 8     8's children have no children.                stack = [3]
    pop 3     1 and 4 are leaves, so 3 does not count.      stack = [1, 4]
    pop 4, 1  leaves
    result = [5]

Print if smaller than m. The job is one comparison.

    while stack:
        curr = stack.pop()
        if curr.item < m:
            print(curr.item, end=" ")
        if curr.left:  stack.append(curr.left)
        if curr.right: stack.append(curr.right)

Smallest value. The job is a running minimum.

    smallest = root.item
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.item < smallest:
            smallest = curr.item
        if curr.left:  stack.append(curr.left)
        if curr.right: stack.append(curr.right)
    return smallest

Mirror. The job is a swap. Push the children after the swap
so both sides still get swapped.

    while stack:
        curr = stack.pop()
        curr.left, curr.right = curr.right, curr.left
        if curr.left:  stack.append(curr.left)
        if curr.right: stack.append(curr.right)

Preorder print is this same loop. Push right, then left, and print on pop.
That version is in walking_notes.md.


WHEN THIS LOOP IS THE WRONG TOOL
--------------------------------
The children's answers have to come back before you can finish yourself.
Height, a great-grandchild, identical trees, a subtree sum.

    height(me) = 1 + max(height(left), height(right))

Recursion does that: the call returns, then you use the number.
The loop above cannot, because it finishes curr before the children run.
Those questions stay recursive. hasGreatGrandchild is one of them.
A grandchild check is the loop above. A great-grandchild needs the height.

Postorder also finishes the children before me.
Do not force it into this loop. Use the reverse or the two-stack walk
in walking_notes.md.

Level order is a queue, not this stack. Pop from the front.
That code is in walking_notes.md.
Zigzag is the same queue, with every other row reversed.
Try zigzag_level_try.py.


TWO THINGS TO KEEP APART
------------------------
stack   who still needs a visit
result  the answer

Push a child only when it exists. Popping None and reading .val crashes.
Push the child, not curr again. Pushing yourself never ends.

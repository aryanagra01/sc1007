LINKED LIST NOTES (Tut + Lab)
=============================

BASICS
------
- Node has .data and .next (doubly also has .prev)
- head = first node, traverse with cur = cur.next
- findNode(index) = walk index steps from head
- insert at 0: new_node.next = head, head = new_node
- remove: need node BEFORE target (prev.next = cur.next)


REVERSING LINKED LIST
---------------------
1) use 3 pointers: prev, cur, next

    prev = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    return prev   # prev is the new head

2) memory trick: "save next, flip, advance both"
    - save next (so you don't lose the rest of the list)
    - point cur.next backward to prev
    - shift prev and cur one step forward

3) for doubly linked — same thing
    a) except add in the line cur.prev = next_node (before cur.next = prev)
    b) full loop:
        while cur:
            next_node = cur.next
            cur.prev = next_node
            cur.next = prev
            prev = cur
            cur = next_node
        return prev


DOUBLY LINKED LIST — INSERT AT INDEX
------------------------------------
1) index 0 (front):
    new_node.next = head
    if head:
        head.prev = new_node
    head = new_node

2) middle or end (index > 0):
    walk to node at (index - 1) → call it current
    new_node.next = current.next
    new_node.prev = current
    if current.next:
        current.next.prev = new_node
    current.next = new_node


DOUBLY LINKED LIST — DELETE
---------------------------
1) delete by index 0:
    head = head.next
    if head:
        head.prev = None

2) delete by index (middle/end):
    walk to node at index → call it current
    current.prev.next = current.next
    if current.next:
        current.next.prev = current.prev

3) delete by value (walk until found):
    if current.prev:
        current.prev.next = current.next
    else:
        head = current.next          # deleting head
    if current.next:
        current.next.prev = current.prev


FAST/SLOW + PREV (middle, palindrome, delete middle)
----------------------------------------------------
    prev = None
    slow = fast = head
    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next
        fast = fast.next.next

When loop stops:
- ODD (e.g. 1→2→3→2→1):
    slow = exact middle (3)
    prev = node before middle (2)
- EVEN (e.g. 1→2→2→1):
    slow = 1st node of 2nd half (2nd 2)
    prev = last node of 1st half (1st 2) ← one BEFORE 2nd half starts

Example EVEN 1→2→2→1:
    after loop → prev=1st 2, slow=2nd 2

Example ODD 1→2→3→2→1:
    after loop → prev=2, slow=3


DELETE MIDDLE NODE
------------------
Use slow/fast WITH prev (see above). Delete slow.

    prev = None
    slow = fast = head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # delete slow
    if prev:
        prev.next = slow.next
    else:
        head = slow.next    # list had 1 node only

EVEN vs ODD for delete middle:
- ODD:  slow IS the middle → delete it (use prev to skip over it)
- EVEN: slow = start of 2nd half, prev = last of 1st half
        delete slow (right-middle) via prev.next = slow.next
        prev is the node one before 2nd half — that's your even anchor


PALINDROME CHECKING
-------------------
3 steps: find middle → reverse 2nd half → compare

1) slow/fast to find start of 2nd half (no prev needed here)
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

2) reverse from slow (same reverse algo, prev starts as None)
    prev = None
    cur = slow
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

3) compare front vs prev
    front = head
    while prev is not None:
        if prev.data != front.data:
            return False
        prev = prev.next
        front = front.next
    return True

EVEN vs ODD length (palindrome):
- ODD (e.g. 1→2→3→2→1): slow stops ON middle (3). Reverse includes middle.
  Middle compares with itself once — always passes.
- EVEN (e.g. 1→2→2→1): slow stops on 1st node of 2nd half (2nd 2). Clean 50/50 split.

Why prev = None when reversing? NOT because we stopped in middle — any reverse starts
with prev=None because the first node reversed becomes the tail (must point to None).


FLOYD CYCLE DETECTION (loop check)
----------------------------------
Use when list might loop back (cycle). Two pointers, fast moves 2x slow.

1) Detect cycle:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return 0   # no cycle

2) Measure cycle length (after they meet):
    length = 1
    cur = slow.next
    while cur is not slow:
        cur = cur.next
        length += 1
    return length

Alt: hashmap/dict — store each node seen, return when revisit. O(n) space.
Floyd is O(1) space — preferred for exams.


TWO SUBLISTS + RECONNECT (partition by value)
---------------------------------------------
Used for: move evens first / odds back, move odd items to back (lab)

    even_head = even_tail = None
    odd_head = odd_tail = None
    cur = head

    while cur:
        next_node = cur.next
        cur.next = None          # detach node

        if cur.data % 2 == 0:
            if even_head is None:
                even_head = even_tail = cur
            else:
                even_tail.next = cur
                even_tail = cur
        else:
            if odd_head is None:
                odd_head = odd_tail = cur
            else:
                odd_tail.next = cur
                odd_tail = cur
        cur = next_node

    if even_head is None:
        return odd_head
    even_tail.next = odd_head
    return even_head


FIND NODE + UNLINK/RELINK (move max OR move min to front)
---------------------------------------------------------
Same pattern for both — only difference is what you search for.

MOVE MAX:
    walk list, track max_node AND pre_max (node before max)
    if pre_max is None → max already at front, done
    else:
        pre_max.next = max_node.next
        max_node.next = head
        head = max_node

MOVE MIN (same relink, different search):
    pass 1: find min value
    pass 2: walk again, when cur.next is min → unlink and prepend to front
        moving_node = cur.next
        cur.next = cur.next.next
        moving_node.next = head
        head = moving_node
    (if min already at head, nothing to do)


MERGE TWO SORTED LISTS
----------------------
Use dummy head so you don't special-case the first node.

    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2   # attach leftover
    return dummy.next


REMOVE DUPLICATES (sorted list only!)
-------------------------------------
Single pass — duplicates are adjacent when sorted.

    cur = head
    while cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next


MOVE EVENS TO BACK (tutorial version)
-------------------------------------
Traverse with index. When even found: remove it, append to end.

    index = 0
    cur = head
    for _ in range(size):
        if cur.data % 2 == 0:
            val = cur.data
            cur = cur.next           # move BEFORE remove
            removeNode(index)        # index stays same
            insertNode(val, size)
        else:
            index += 1
            cur = cur.next


SPLIT BY INDEX (not by value!) — lab split_even_odd
---------------------------------------------------
Split positions 0,2,4... vs 1,3,5... (NOT even/odd numbers)

    i = 0
    cur = head
    while cur:
        if i % 2 == 0:
            even_list.append(cur.data)
        else:
            odd_list.append(cur.data)
        i += 1
        cur = cur.next


WHICH TECHNIQUE WHEN?
---------------------
Palindrome?              → slow/fast + reverse half + compare
Delete middle?           → slow/fast + prev, delete slow
Cycle / cycle length?    → Floyd (slow/fast)
Partition evens/odds?    → two sublists + reconnect
Merge sorted lists?      → dummy head + compare + attach leftover
Split by index 0,2,4?    → counter i % 2
Remove dupes (sorted)?   → single pass skip matching next
Move max/min to front?   → find node + prev, unlink, prepend
Reverse whole list?      → prev/cur/next loop, return prev
Doubly insert/delete?    → update BOTH next and prev pointers

"""
Stack and queue practice. Fill each function, then run this file.

Stack: push, pop, peek, is_empty, size. The last push is the top.
Queue: enqueue, dequeue, peek, is_empty, size. The first enqueue is the front.

Use one extra stack or queue when the question says so. Do not turn the
whole thing into a Python list inside your answer. Reading .items_top_first
or .items_front_first is only for the checks at the bottom.
"""

from _support import Stack, Queue, check


def reverse_stack(stack):
    """Reverse the stack using one queue.
    Top-first [3, 2, 1] becomes [1, 2, 3].
    """
    raise NotImplementedError


def reverse_first_k(queue, k):
    """Reverse the first k items of the queue. Use one stack.
    Front-first [1, 2, 3, 4, 5], k = 3 -> [3, 2, 1, 4, 5]
    """
    raise NotImplementedError


def reverse_queue_segment(queue, m, n):
    """Reverse index m through n, inclusive. Use one stack.
    [10, 20, 30, 40, 50, 60, 70], m = 2, n = 5 -> [10, 20, 60, 50, 40, 30, 70]
    """
    raise NotImplementedError


def recursive_reverse(queue):
    """Reverse the queue using recursion. No extra stack.
    [1, 2, 3, 4] -> [4, 3, 2, 1]
    """
    raise NotImplementedError


def remove_until(stack, value):
    """Pop until value is on top. If value is already on top, pop nothing.
    If value is not in the stack, the stack ends empty.
    Top-first [1, 2, 3, 4, 5], value 3 -> [3, 4, 5]
    """
    raise NotImplementedError


def delete_middle(stack):
    """Remove the middle item. Use one extra stack.
    Odd length: the centre. Even length: the one just above the centre,
    which is size // 2 pops, then one more pop.
    Top-first [5, 4, 3, 2, 1] -> [5, 4, 2, 1]
    """
    raise NotImplementedError


def interleave(queue):
    """Even length. Alternate the first half with the second half.
    Use one stack. [1, 2, 3, 4, 5, 6] -> [1, 4, 2, 5, 3, 6]
    Odd length: leave the queue as it is.
    """
    raise NotImplementedError


def sort_stack(stack):
    """Sort so the largest value is on top. Use one extra stack.
    Top-first [2, 1, 3] -> [3, 2, 1]
    """
    raise NotImplementedError

    temp = Stack()

    while not stack.isempty():
        data = stack.pop()
        if not temp.isempty and temp.peek < data.data:
            stack.push(temp.pop())
        tmep.push(data)


def balanced(expression):
    """True when (), [], and {} are paired and in the right order.
    "([{}])" -> True
    "[({{)])" -> False
    """
    raise NotImplementedError


def palindrome(word):
    """True if the letters read the same forwards and backwards.
    Ignore spaces and case. Use one stack and one queue.
    "A man a plan a canal Panama" -> True
    "hello" -> False
    """
    raise NotImplementedError


if __name__ == "__main__":
    def do_stack(fn, values, *args):
        stack = Stack(values)
        fn(stack, *args)
        return stack.items_top_first()

    def do_queue(fn, values, *args):
        queue = Queue(values)
        fn(queue, *args)
        return queue.items_front_first()

    check("reverse stack", lambda: do_stack(reverse_stack, [1, 2, 3]), [1, 2, 3])
    check("reverse first k", lambda: do_queue(reverse_first_k, [1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5])
    check("reverse segment", lambda: do_queue(reverse_queue_segment, [10, 20, 30, 40, 50, 60, 70], 2, 5), [10, 20, 60, 50, 40, 30, 70])
    check("recursive reverse", lambda: do_queue(recursive_reverse, [1, 2, 3, 4]), [4, 3, 2, 1])
    check("remove until", lambda: do_stack(remove_until, [5, 4, 3, 2, 1], 3), [3, 4, 5])
    check("delete middle", lambda: do_stack(delete_middle, [1, 2, 3, 4, 5]), [5, 4, 2, 1])
    check("interleave", lambda: do_queue(interleave, [1, 2, 3, 4, 5, 6]), [1, 4, 2, 5, 3, 6])
    check("sort stack", lambda: do_stack(sort_stack, [3, 1, 2]), [3, 2, 1])
    check("balanced yes", lambda: balanced("([{}])"), True)
    check("balanced no", lambda: balanced("[({{)])"), False)
    check("palindrome yes", lambda: palindrome("A man a plan a canal Panama"), True)
    check("palindrome no", lambda: palindrome("hello"), False)

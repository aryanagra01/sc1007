"""
3. findUnion

Given two sorted linked lists, implement a function to create a new linked
list that represents the union of the two original lists. The new linked list
should be created without modifying the original lists.

Constraints:
1. The linked lists are sorted in non-decreasing order (ascending order,
   allowing duplicates).
2. The elements in the linked lists are not necessarily distinct (duplicates
   are allowed in the input lists).
3. The new linked list should contain all unique elements from both input
   linked lists.
4. The order of elements in the union linked list must be the same as they
   appear in the original lists (sorted order).
5. Additional data structures such as lists, dictionaries, sets, or arrays
   are not allowed.

Function prototype:
    def findUnion(head1, head2):

Input format:
    Two space-separated lists of integers representing the two sorted linked
    lists. Each linked list is terminated by a non-numeric character.

Output format:
    A space-separated list of integers representing the union of the two
    linked lists.

Example 1 (basic case with duplicates in input):
    list1 = 1 -> 2 -> 2 -> 3 -> None
    list2 = 2 -> 3 -> 4 -> None
    Union: 1 2 3 4

Example 2 (both lists have unique elements):
    list1 = 1 -> 3 -> 5 -> 7 -> None
    list2 = 2 -> 4 -> 6 -> 8 -> None
    Union: 1 2 3 4 5 6 7 8

Example 3 (one list is a subset of another):
    list1 = 3 -> 3 -> 4 -> 4 -> 5 -> 5 -> 6 -> 6 -> None
    list2 = 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5 -> 5 -> 6 -> 6 -> None
    Union: 1 2 3 4 5 6

Score: 100/100
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def findNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")
        if self.head is None:
            raise ValueError("List is empty")

        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            raise ValueError("Invalid position")

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return True

        prev_node = self.findNode(index - 1)
        if prev_node is not None:
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.size += 1
            return True
        return False

    def removeNode(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Invalid position")

        if self.head is None:
            return False

        if index == 0:
            cur = self.head
            self.head = cur.next
            self.size -= 1
            return True

        pre = self.findNode(index - 1)
        if pre is not None and pre.next is not None:
            cur = pre.next
            pre.next = cur.next
            self.size -= 1
            return True
        return False

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur is not None:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


def findUnion(head1, head2):
    # Write your code here #
    # duplicates allowed, ascending
    # contian all unique elemnets
    # acednig sorted
    # no other data

    # create dummy node
    dummy = Node(0)

    l1 = head1
    l2 = head2
    cur = dummy

    while l1 and l2:
        if cur.data == l1.data:
            l1 = l1.next
        elif cur.data == l2.data:
            l2 = l2.next
        elif l1.data <= l2.data:
            cur.next = Node(l1.data)
            l1 = l1.next
            cur = cur.next
        else:
            cur.next = Node(l2.data)
            l2 = l2.next
            cur = cur.next

    if l1:
        while l1:
            if l1.data == cur.data:
                l1 = l1.next
            else:
                cur.next = Node(l1.data)
                l1 = l1.next
                cur = cur.next
    elif l2:
        while l2:
            if cur.data == l2.data:
                l2 = l2.next
            else:
                cur.next = Node(l2.data)
                l2 = l2.next
                cur = cur.next

    return dummy.next


if __name__ == "__main__":
    # Helper function to create a linked list from a string of space-separated numbers
    def create_linked_list_from_input(input_string):
        linked_list = LinkedList()
        numbers = []
        for item in input_string.split():
            try:
                numbers.append(int(item))
            except ValueError:
                continue

        for i, num in enumerate(numbers):
            linked_list.insertNode(num, i)

        return linked_list

    # Read input from file (or stdin if redirect is used)
    try:
        # Read first line for first linked list
        input_str1 = input()
        list1 = create_linked_list_from_input(input_str1)

        # Read second line for second linked list
        input_str2 = input()
        list2 = create_linked_list_from_input(input_str2)

        # Find the union
        result = findUnion(list1.head, list2.head)

        # Print the union list
        if result is None:
            print("No elements")
        else:
            temp = result
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    except EOFError:
        print("Error: Input file should contain at least two lines with the linked lists data.")

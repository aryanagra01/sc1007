from unittest.result import failfast


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

    def printList(self):
        cur = self.head
        if cur is None:
            print("Empty")
            return
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


class Solution:
    def cycleLength(self, head):
        #--------- MODIFY NOTHING ABOVE THIS LINE OR YOUR SOLTUION WILL GET 0 MARKS ---------#
        # Write your program here #
        
        #save dictionary solution
        # current = head
        # savedValues = {}
        # index = 0

        # while current is not None:
        #     if current in savedValues:
        #         return index - savedValues[current]
        #     else:
        #         savedValues[current] = index
        #         current = current.next
        #         index += 1

        # return 0

        #aryan attempt with 2 pointers
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                lenght = 1
                slow = slow.next
                while slow is not fast:
                    slow = slow.next
                    lenght += 1
                return lenght

        return 0


        #Better Solution with O(1) space complexity
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:                    # cycle found — measure it
                length = 1
                cur = slow.next
                while cur is not slow:
                    cur = cur.next
                    length += 1
                return length

        return 0                                # fast hit None — no cycle

        #--------- MODIFY NOTHING BELOW THIS LINE OR YOUR SOLTUION WILL GET 0 MARKS ---------#

#==============================================================================================
if __name__ == "__main__":

    # Helper function to create a linked list from input
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

    try:
        # Read linked list elements
        input_str = input()
        linked_list = create_linked_list_from_input(input_str)

        # Read index to create cycle (-1 means no cycle)
        cycle_index = int(input())

        # Create cycle if required
        if cycle_index != -1:
            last_node = linked_list.findNode(linked_list.size - 1)
            cycle_node = linked_list.findNode(cycle_index)
            last_node.next = cycle_node

        # Find and print cycle length
        result = Solution().cycleLength(linked_list.head)   
        print(result)

    except EOFError:
        print("Error: Input should contain the list elements and a cycle index.")

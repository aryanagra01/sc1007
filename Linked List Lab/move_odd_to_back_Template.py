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


class Solution:
    def moveOdditemstoback(self, head):
        #--------- MODIFY NOTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS ---------#

        # THIS IS NOT CORRECT YET
        #         current = head
        # oddLinkedList = LinkedList()
        # evenLinkedList  = LinkedList()
        # index = 0

        # while current != None:
        #     if current.data % 2 == 0:
        #         evenLinkedList.insertNode(current.data, evenLinkedList.size)
        #     else:
        #         oddLinkedList.insertNode(current.data, oddLinkedList.size)

        # current = evenLinkedList.head
        # while current.next is not None:
        #     current = current.next
        # current.next = oddLinkedList.head
        # return evenLinkedList.head

        
        even_head = None
        even_tail = None
        odd_head = None
        odd_tail = None
        cur = head

        while cur is not None:
            next_node = cur.next
            cur.next = None
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
        else:
            even_tail.next = odd_head
            return even_head
            





        #--------- MODIFY NOTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS ---------#


#==============================================================================================
if __name__ == "__main__":
    # Reads one line of space-separated integers, e.g.:
    #
    #   Enter numbers: 1 2 3 4 5 6
    #
    # Builds the list via insertNode, moves odd values to the back
    # (evens keep their relative order first, then odds), and prints
    # the resulting list.
    #
    # Run with:
    #   python3 move_odd_to_back.py

    line = input("Enter numbers: ").strip()
    nums = [int(tok) for tok in line.split()] if line else []

    # --- run_test logic, inlined directly here ---
    linked_list = LinkedList()

    for i, num in enumerate(nums):
        linked_list.insertNode(num, i)

    sol = Solution()
    linked_list.head = sol.moveOdditemstoback(linked_list.head)

    result = []
    cur = linked_list.head
    while cur is not None:
        result.append(cur.data)
        cur = cur.next
    # --- end run_test logic ---

    print(result)
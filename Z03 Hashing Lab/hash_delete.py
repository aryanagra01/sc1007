
LOAD_FACTOR = 3  # Define global load factor


def menu():
    print("============= Hash Table ============")
    print("|1. Create a hash table             |")
    print("|2. Insert a key to the hash table  |")
    print("|3. Search a key in the hash table  |")
    print("|4. Delete a key from the hash table|")
    print("|5. Print the hash table            |")
    print("|6. Quit                            |")
    print("=====================================")


class ListNode:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None

    def findNode(self, index):
        if index < 0 or index >= self.size:
            return None
        cur = self.head
        while index > 0:
            cur = cur.next
            index -= 1
        return cur

    def insertNode(self, data, index):
        if index < 0 or index > self.size:
            return False

        new_node = ListNode(data)

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
            return False

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return True

        prev_node = self.findNode(index - 1)
        if prev_node is not None and prev_node.next is not None:
            prev_node.next = prev_node.next.next
            self.size -= 1
            return True
        return False

    def search(self, key):
        cur = self.head
        index = 0
        while cur:
            if cur.item == key:
                return index
            cur = cur.next
            index += 1
        return None

    def printList(self):
        cur = self.head
        while cur:
            print(cur.item, end=" -> ")
            cur = cur.next
        print("None")


class HashTable:
    def __init__(self, num_data, load_factor=LOAD_FACTOR):
        self.load_factor = load_factor
        self.size = max(1, num_data // self.load_factor)
        self.table = [LinkedList() for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def hash_insert(self, key):
        index = self.hash_function(key)
        if self.hash_search(key) is not None:
            return False
        return self.table[index].insertNode(key, 0)

    def hash_search(self, key):
        index = self.hash_function(key)
        return self.table[index].search(key)

    def hash_delete(self, key):
        # : Implement your solution here THE QUESTION IS HERE
        
        index = self.hash_function(key)
        llIndex = self.hash_search(key)
        #index will alwyas be true with a key, but ll no bcaeu it may not be inside
        if llIndex is None:
            return False
        return self.table[index].removeNode(llIndex)
        

    def display(self):
        for i in range(self.size):
            print(f"Slot {i}: ", end="")
            self.table[i].printList()


if __name__ == "__main__":
    opt = 0
    hash_table = None
    menu()

    while True:
        opt = int(input("Enter selection: "))

        if opt == 1:
            size = int(input("Enter number of data to be inserted: "))
            hash_table = HashTable(size, LOAD_FACTOR)
            print("HashTable is created.")
        elif opt == 2:
            if hash_table is None:
                print("Please create a hash table first.")
                continue
            key = int(input("Enter a key to be inserted: "))
            if hash_table.hash_insert(key):
                print(f"{key} is inserted.")
            else:
                print(f"{key} is a duplicate. No key is inserted.")
        elif opt == 3:
            if hash_table is None:
                print("Please create a hash table first.")
                continue
            key = int(input("Enter a key for searching in the HashTable: "))
            index = hash_table.hash_search(key)
            if index is not None:
                print(f"{key} is found at index {index}.")
            else:
                print(f"{key} is not found.")
        elif opt == 4:
            if hash_table is None:
                print("Please create a hash table first.")
                continue
            key = int(input("Enter a key to be deleted: "))
            if hash_table.hash_delete(key):
                print(f"{key} is deleted.")
            else:
                print(f"{key} is not found.")
        elif opt == 5:
            if hash_table is None:
                print("Please create a hash table first.")
                continue
            hash_table.display()
        elif opt == 6:
            print("Exiting program.")
            break
        else:
            print("Invalid selection, please try again.")

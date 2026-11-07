class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class HashTable:
    def __init__(self, num_data):
        self.load_factor = 3
        self.size = max(1, num_data // self.load_factor)  # Ensure at least one slot
        self.table = [None] * self.size  # Initialize an array of linked lists

    def _hash(self, key):
        return hash(key) % self.size

    def hash_insert(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return
            current = current.next

        new_node = Node(key)
        new_node.next = self.table[index]
        self.table[index] = new_node
        

    def hash_search(self, key):
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next

        return False

    def hash_print(self):
        print("Hash Table:")
        for i, node in enumerate(self.table):
            print(f"Slot {i}: ", end="")
            current = node
            while current:
                print(f"{current.key} -> ", end="")
                current = current.next
            print("None")


# Menu-driven program
if __name__ == "__main__":
    print("============= Hash Table ============")
    print("|1. Create a hash table             |")
    print("|2. Insert a key to the hash table  |")
    print("|3. Search a key in the hash table  |")
    print("|4. Print the hash table            |")
    print("|5. Quit                            |")
    print("=====================================")

    ht = None

    while True:
        opt = int(input("Enter selection: "))
        if opt == 1:
            size = int(input("Enter number of data to be inserted: "))
            ht = HashTable(size)
            print("HashTable is created.")
        elif opt == 2:
            if ht is None:
                print("Create a hash table first!")
            else:
                key = int(input("Enter a key to be inserted: "))
                if ht.hash_insert(key):
                    print(f"{key} is inserted.")
                else:
                    print(f"{key} is a duplicate. No key is inserted.")
        elif opt == 3:
            if ht is None:
                print("Create a hash table first!")
            else:
                key = int(input("Enter a key for searching in the HashTable: "))
                if ht.hash_search(key):
                    print(f"{key} is found.")
                else:
                    print(f"{key} is not found.")
        elif opt == 4:
            if ht is None:
                print("Create a hash table first!")
            else:
                ht.hash_print()
        elif opt == 5:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")
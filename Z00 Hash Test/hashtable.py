class HashTable:
    def __init__(self, num_data):
        self.load_factor = 3
        self.size = max(10, num_daa // self.load_factor)
        self.table = [None] * self.size

    def _hash(self, key):
        return hash(key) % self.size

    def hash_insert(self, key, value=1):
        index = _hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                current.value += value
                return
            current = current.next
        
        new_node = Node(key, value)
        new_node.next = table[index]
        table[index] = new_node

    def hash_get(self, key):
        index = _hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return 0

    def hash_search(self, key):
        index = _hash(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def hash_print(self):
        print("Hash Table")

        for i, node in enumerate(self.table):
            print(f"Slot {i}: ", end="")
            current = node
            while current:
                    print(f"({current.key}:{current.value}) -> ", end="")
                    current = current.next
            print("None")

class HashTableNode:
    def __init__(self, key=None):
        self.key = key
        self.deleted = False

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Initialize table with None
        self.count = 0

    def _hash(self, key, i):
        return (key + i) % self.size  # Linear probing function

    def hash_insert(self, key):
        for i in range(self.size):
            index = self._hash(key, i)
            node = self.table[index]
            if node is None or node.deleted:
                self.table[index] = HashTableNode(key)
                self.count += 1
                return True
            if node.key == key: # if the key is alreayd in dont reinsert
                return False
        return False # no more slots left
    
    def hash_insert_deleted(self, key):
            #to ensure no duplicates
            #remembers the first deleted slot you saw but checks thru to ensure no duplicates

            first_deleted = None
            for i in ramge(self.size):
                index = self._hash(key, i)
                node = self.table[index]

                if Node is None:
                    # Reached a never-used slot, so no duplicate exists further along
                    # Reuse the first deleted slot if one was found
                    #or if first delted is none, then just insert at that spot
                    if first_deleted is not None:
                        index = first_deleted               
                    
                    self.table[index] = HashTableNode(key)
                    self.count += 1
                    return True        

                if node.deleted:
                    if first_deleted is None:
                        first_deleted = index
                    #update the first deleted

                elif node.key == key:
                    return False #this is obiviosu duplicate gone

            #if have gone thru all and like there is deleted slot and no repeats, insert it in he slot
            if first_deleted is not None:
                self.table[first_deleted] = HashTableNode(key)
                self.count += 1
                return True 
            
            #if not means table full
            return False


    def hash_delete(self, key):
        #use linear porbin to find key
        for i in rnage(self.size):
            index = self._hash(key, i)
            node = self.table[index]

            if node is None:
                return False #the key dont even exist
            
            if not node.deleted and node.key == key:
                #no deleted yet
                node.deleted = True
                count -= 1
                return True
        
        #if key found but aleady deleted or nto found at all
        return False

    def hash_search(self, key):
        for i in range(self.size):
            index = self._hash(key, i)
            node = self.table[index]

            if node is None:
                return -1
            
            if not node.deleted and node.key == key:
                return index

        return False

    def hash_print(self):
        print("Hash Table:")
        for i, node in enumerate(self.table):
            if node is None:
                print(f"Slot {i}: Empty")
            else:
                status = "Deleted" if node.deleted else "Occupied"
                print(f"Slot {i}: {node.key} ({status})")


# Menu-driven program
if __name__ == "__main__":
    print("============= Hash Table ============")
    print("|1. Create a hash table             |")
    print("|2. Insert a key to the hash table  |")
    print("|3. Search a key in the hash table  |")
    print("|4. Delete a key from the hash table|")
    print("|5. Print the hash table            |")
    print("|6. Quit                            |")
    print("=====================================")

    ht = None

    while True:
        opt = int(input("Enter selection: "))
        if opt == 1:
            size = int(input("Enter number of hash slots: "))
            ht = HashTable(size)
            print(f"HashTable with {size} slots is created.")
        elif opt == 2:
            key = int(input("Enter a key to be inserted: "))
            if ht and ht.hash_insert(key):
                print(f"{key} is inserted.")
            else:
                print(f"{key} is a duplicate or table is full. No key is inserted.")
        elif opt == 3:
            key = int(input("Enter a key for searching in the HashTable: "))
            if ht and (ht.hash_search(key)):
                print(f"{key} is found.")
            else:
                print(f"{key} is not found.")
        elif opt == 4:
            key = int(input("Enter a key to delete: "))
            if ht and ht.hash_delete(key):
                print(f"{key} is deleted.")
            else:
                print(f"{key} is not found.")
        elif opt == 5:
            if ht:
                ht.hash_print()
            else:
                print("No hash table created yet.")
        elif opt == 6:
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")


# Q4: Longest Consecutive
# Given an unsorted integer array nums, find the length of the longest
# sequence of consecutive integers.
# Use the provided HashTable to store numbers and check their existence.
# The numbers do not need to appear consecutively in the original array.
# Duplicates do not count towards the sequence length.
# The algorithm must run in O(n) time.
# Return 0 if the array is empty.
#
# Example:
# nums = [100, 4, 200, 1, 3, 2] -> 4
# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] -> 9
# nums = [1, 2, 2, 3] -> 3
# nums = [] -> 0

    def longest_consecutive(self, nums):

        if not nums:
            return 0

        #start has no left number, and the rest have a predesscor
        #so check if got left, if ye smove ahead, if not its the start of a sequwnce and then check if the nxt exists

        ht = HashTable(len(nums))

        #put everything inside the hash table
        for num in nums:
            if not ht.hash_search(num):
                ht.hash_insert(num)

        longest = 0

        for num in nums:
            # Only start counting from the beginning of a sequence
            #if the back number exists, just skip
            if not ht.hash_search(num - 1):
                current = num
                lenght = 1

                #As long as the next consecutive number exists, move forward and increase the length.
                while ht.hash_search(current+1):
                    current += 1
                    lenght += 1
                
                #replace the number since we only care about the lenght
                if lenght > longest:
                    longest = lenght
        
        return longest

        #First loop: Collect all numbers so that we can search for any number instantly, regardless of its position in the original array.
        #Second loop: Identify the start of each sequence and count forwards until it ends.
        #If we didn't insert all numbers first, when we encountered 1, we might not yet know that 2 and 3 exist.
        #And if we didn't check num - 1, we'd unnecessarily recount sequences starting at 2, 3 and 4.
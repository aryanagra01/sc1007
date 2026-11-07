
# Q2: Two Sum
# Given an array nums and a target, find two different indices whose values sum to target.
# Use the provided HashTable to store previously seen numbers and their indices.
# For each number, check whether its complement (target - nums[j]) already exists.
# Use hash_search() to check for existence and hash_get() to retrieve the index.
# Only insert a number if it has not been seen before.
# Return [i, j] where i < j. Exactly one valid answer is guaranteed.
#
# Example:
# nums = [2, 7, 11, 15], target = 9 -> [0, 1]
# nums = [3, 3], target = 6       -> [0, 1]
    
    
    def two_sum(self, nums, target):
        ht = HashTable(len(nums))

        for index, number in enumerate(nums):
            want = target - number

            if ht.hash_search(want):
                want_index = ht.hash_get(want)
                return [want_index, index]

            if not ht.hash_search(number):
                ht.hash_insert(number, index)
    
    
    def two_sum(self, nums, target):
        ht = HashTable(len(nums))

        for i, num in enumerate(nums):
            complement = target - num

            if ht.hash_search(complement):
                return [ht.hash_get(complement), i]

            if not ht.hash_search(num):
                ht.hash_insert(num, i)
        return []


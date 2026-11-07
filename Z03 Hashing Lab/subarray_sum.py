# Q3: Count Subarrays
# Given an integer array nums and an integer k, count the number of
# continuous subarrays whose sum equals k.
# Use a HashTable to store prefix sums and their frequencies.
# A subarray sums to k when current_prefix_sum - previous_prefix_sum = k.
# The algorithm must run in O(n) time.
# Return the total number of valid subarrays.
#
# Example:
# nums = [1, 1, 1], k = 2 -> 2
# nums = [1, 2, 3], k = 3 -> 2
# nums = [1, -1, 0], k = 0 -> 3

#find the preix and see if you chop off another prefix vlaue from below it to get the subset needed
#thats why O(n) --> calcaute prefix for each and then check if the subtraction required exsits below it
#create an empty prefix with count of 1 in case the things add up to k
#count exists becaseu there can be multiple eariler prefixes whih the same value, hence multiple ways

    def subarray_sum(self, nums, k):
        ht = HashTable(len(nums) + 1)
        ht.hash_insert(0, 1)
        
        result = 0
        prefixSum = 0

        for num in nums:

            #add the new number to the total prefix sum
            prefixSum += num
            #find the diff to check if its inside
            target = prefixSum - k 
            
            #if zero then nothing get added so its chill
            #if got multiple prefixes that get to the taregt, then add all becaseu count is updated
            result += ht.hash_get(target)

            #either add or increase the vlaue of the count of the number of prefixes that get the sm
            ht.hash_insert(prefixSum)

        return result

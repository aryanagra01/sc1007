
# Question: First Occurrence in a Sorted Array
#
# Given a sorted array of integers (possibly containing
# duplicates), find the index of the FIRST occurrence
# of a given target number.
#
# Return -1 if the target is not present.
#
# Example:
# arr = [1, 2, 2, 2, 3, 4]
# target = 2
# Output: 1
#
# Requirements:
# - Use binary search, not brute force.
# - Expected time complexity: O(log n)
# - Return the index (0-based), not the value.

   
def first_occurrence(arr, target):

    low, high = 0, len(arr) - 1
    leftmost = -1

    while low <= high:
        mid = (low + high) // 2
        
        #save in leftmost and just keep binary searching to the left until the low high cross
        if arr[mid] == target:
            leftmost = mid
            high = mid - 1

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return leftmost



# Test cases
print(first_occurrence([1, 2, 2, 2, 3, 4], 2))  # Expected: 1
print(first_occurrence([1, 2, 3, 4, 5], 3))     # Expected: 2
print(first_occurrence([1, 2, 3, 4, 5], 6))     # Expected: -1
print(first_occurrence([2, 2, 2, 2], 2))        # Expected: 0
print(first_occurrence([], 2))                  # Expected: -1
# Q: Find the Smallest Number Greater Than the Target (Binary Search)

# Given a sorted array of integers (no duplicates) and a target x,
# find the smallest number in the array that is strictly greater than x.

# If no such number exists, return -1.

# Required time complexity: O(log n)

# Example 1:
# arr = [1, 2, 3, 4, 5], x = 3
# Output: 4

# Example 2:
# arr = [1, 2, 3, 4, 5], x = 9
# Output: -1

# Example 3:
# arr = [2, 5, 8, 12, 16], x = 6
# Output: 8


def find_smallest_greater(arr, x):


    low, high = 0, len(arr) - 1
    smallestGreater = -1 #default

    while low <= high:

        mid = (low+high) // 2

        if arr[mid] <= x:
            # Current element and everything to its left cannot be the answer
            low = mid + 1
        else:
            #no need to check becaseu we found a possible answer already, and then low = high would deffo run to update this
            smallestGreater = arr[mid]
            # Keep searching left for a potentially smaller valid answer
            high = mid - 1
    
    return smallestGreater


# Test cases
print(find_smallest_greater([1, 2, 3, 4, 5], 3))   # 4
print(find_smallest_greater([1, 2, 3, 4, 5], 9))   # -1
print(find_smallest_greater([2, 5, 8, 12, 16], 6)) # 8
print(find_smallest_greater([1, 3, 5, 7], 0))      # 1
print(find_smallest_greater([1, 3, 5, 7], 7))      # -1
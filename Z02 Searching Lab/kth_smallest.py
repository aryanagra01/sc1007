
# Question: Kth Smallest Element in a Sorted Matrix
#
# Given an n x n matrix where every row and every column
# is sorted in non-decreasing order, return the kth
# smallest element.
#
# Duplicates count as separate elements.
#
# Example:
# matrix = [
#     [1,  5,  9],
#     [10, 11, 13],
#     [12, 13, 15]
# ]
# k = 5
#
# Expected output: 11
#
# Note:
# The 7th and 8th smallest elements are both 13.
#
# Try to take advantage of the sorted rows and columns.


def kth_smallest_linear(matrix, k):
    n = len(matrix)

    low = matrix[0][0]
    high = matrix[n-1][n-1]

    #becaseu we are equating the high to be mid, hence it might get stuck in an infinite loop
    while low < high:
        mid = (low + high) // 2

        #count the number of numbers below
        count = 0
        row = n-1
        col = 0

        while row >= 0 and col <= n-1:
            if matrix[row][col] <= mid:
                count += row + 1
                col += 1
            else:
                row -= 1
        
        if count < k:
            low = mid + 1
        else:
            high = mid

    return low


# Test cases
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

print(kth_smallest_linear(matrix, 5))  # Expected: 11
print(kth_smallest_linear(matrix, 7))  # Expected: 13
print(kth_smallest_linear(matrix, 8))  # Expected: 13
print(kth_smallest_linear([[1]], 1))   # Expected: 1
print(kth_smallest_linear([[1, 2], [1, 3]], 2))  # Expected: 1

from typing import List

class Solution:
    def dual_sorted_search(self, A: List[int], K: int) -> List[int]:
        #must run in O(n)
        #2 pointers but start in opposite ends

        left, right = 0, len(A) - 1

        while left <= right:
            total = A[left] + A[right]
            if total == K:
                return[left, right]
            elif total < K:
                left += 1
            else:
                right -= 1
        
        return [-1, -1]

if __name__ == "__main__":
    print("Sorted Dual Search Program")
    print("==========================")
    while True:
        values = input("\nEnter the sorted array elements separated by spaces (blank line to quit): ").split()
        if not values:
            break
        try:
            A = [int(v) for v in values]
            K = int(input("Enter the target sum K: "))
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        dual_index = Solution().dual_sorted_search(A, K)
        if not dual_index or dual_index == [-1, -1]:
            print("No pair found.")
        else:
            i, j = dual_index
            print(f"Pair found at indices: {dual_index}")
            print(f"Elements: {A[i]} + {A[j]} = {K}")

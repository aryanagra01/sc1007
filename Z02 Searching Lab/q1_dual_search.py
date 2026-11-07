from typing import List

class Solution:
    def dual_search(self, A: List[int], K: int) -> List[int]:
        #this is 2 pointer basically
        #i and j both start 
        #i from 0 to lenght
        #j from i to lenght

        lenght = len(A)

        for i in range(lenght):
            for j in range(i, lenght):
                if A[i] + A[j] == K:
                    return [i, j]
        #if nothing found
        return [-1, -1]

if __name__ == "__main__":
    print("Dual Search Program")
    print("===================")
    while True:
        values = input("\nEnter the array elements separated by spaces (blank line to quit): ").split()
        if not values:
            break
        try:
            A = [int(v) for v in values]
            K = int(input("Enter the target sum K: "))
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        dual_index = Solution().dual_search(A, K)
        if not dual_index or dual_index == [-1, -1]:
            print("No pair found.")
        else:
            i, j = dual_index
            print(f"Pair found at indices: {dual_index}")
            print(f"Elements: {A[i]} + {A[j]} = {K}")

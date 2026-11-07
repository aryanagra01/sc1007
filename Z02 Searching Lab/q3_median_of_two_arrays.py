from typing import List

class Solution:
    def find_median_sorted_arrays(self, num1: List[int], num2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A 
        
        l, r = 0, len(A) - 1

        while l <= r:
            i = (l + r) // 2 #A
            j = half - i - 2 #because arrays are indexed at zero

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if (j+1) < len(A) else float('inf')

            #partitiion is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                
                max(Aleft, Bleft) + min(Aright, Bright) / 2
            
            elif Aleft > Bright:
                r = i -1
            else:
                l = i + 1


if __name__ == "__main__":
    print("Median of Two Sorted Arrays Program")
    print("===================================")
    while True:
        first = input("\nEnter the first sorted array separated by spaces (q to quit): ").strip()
        if first.lower() == "q":
            break
        second = input("Enter the second sorted array separated by spaces: ").strip()
        try:
            num1 = [int(v) for v in first.split()]
            num2 = [int(v) for v in second.split()]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue
        if not num1 and not num2:
            print("At least one array must be non-empty.")
            continue
        if num1 != sorted(num1) or num2 != sorted(num2):
            print("Both arrays must be sorted in ascending order.")
            continue

        print("Median:", Solution().find_median_sorted_arrays(num1, num2))

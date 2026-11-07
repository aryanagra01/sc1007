from typing import List

class Solution:
    def find_peak(self, nums: List[int]) -> int:
        # -------- DO NOT MODIFY ANYTHING ABOVE THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------
        # Write your code here #
        pass
        # -------- DO NOT MODIFY ANYTHING BELOW THIS LINE OR YOUR SOLUTION WILL GET 0 MARKS --------

if __name__ == "__main__":
    print("Find Peak Element Program")
    print("=========================")
    while True:
        values = input("\nEnter the array elements separated by spaces (blank line to quit): ").split()
        if not values:
            break
        try:
            nums = [int(v) for v in values]
        except ValueError:
            print("Invalid input! Please enter integers only.")
            continue

        peak_index = Solution().find_peak(nums)
        print("Peak index:", peak_index)
        if peak_index is not None and 0 <= peak_index < len(nums):
            print("Peak value:", nums[peak_index])

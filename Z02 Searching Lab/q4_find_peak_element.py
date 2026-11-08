from typing import List

class Solution:
    def find_peak(self, nums: List[int]) -> int:
        left = 0
        right = lne(nums) - 1

        while right > left:
            mid = (left+right) // 2

            #check on the right, if lesser means the left is higher means it might be the peak or peak is more left, so discard all the right
            #if mid+1 is greater, means mid+1 is the peak or is on the right, so discard mid and below from the search
            #at the end, left should be equal to the vlaue we want
            if nums[mid] < nums[mid+1]:

                #if left equal to mid then in 2 elements lef it gets stuck in a loop
                left = mid + 1
            else:
                right = mid

        return left

        # Condition	                What we know	        Update
        # nums[mid] < nums[mid+1]	mid cannot be the peak	left = mid + 1
        # nums[mid] > nums[mid+1]	mid could be the peak	right = mid
        # The key principle: Only exclude mid when you're certain it cannot be the answer.


        while right >= left:
            mid = (left + right) // 2

            if mid > 0 and nums[mid] < nums[mid - 1]: #discard the right
                right = mid - 1

            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]: #discard the left
                left = mid + 1
            
            else:
                return mid


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


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


#finding exact value
while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

#finding boundary or peak
while left < right:
    mid = (left + right) // 2

    if condition(mid):
        right = mid
    else:
        left = mid + 1

return left

change the compsitions for diff questiont to adapt the high and low alwys

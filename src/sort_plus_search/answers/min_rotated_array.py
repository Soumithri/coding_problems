
def find_min(nums):
    if not nums:
        return -1
    left, right = 0, len(nums)-1
    while left < right:

        mid = left + (right-left)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[right]

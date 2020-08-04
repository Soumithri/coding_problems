
def twoSum(nums, target):
    nums_set = set()
    for i in nums:
        diff = target - i
        if diff in nums_set:
            return True
        else:
            nums_set.add(i)
    return False

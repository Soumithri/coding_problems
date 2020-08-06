
def binary_search(target, num_list):

    if not target:
        raise Exception
    if not num_list:
        raise Exception
    left, right = 0, len(num_list)-1
    mid = left + (right - left)//2

    while left <= right:
        mid = left + (right - left)//2
        if num_list[mid] == target:
            return True
        elif num_list[mid] < target:
            left = mid + 1
        else:
            right = mid
    return False

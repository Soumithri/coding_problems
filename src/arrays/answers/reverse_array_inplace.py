
def reverse_array(char_list):

    left, right = 0, len(char_list) - 1
    while left < right:
        if char_list[left] == char_list[right]:
            continue
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

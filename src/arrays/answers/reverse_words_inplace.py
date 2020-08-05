
def reverse_words(message):
    reverse_characters(message, 0, len(message)-1)
    current_word_start_index = 0
    for i in range(len(message)+1):
        if i == len(message):
            reverse_characters(message, current_word_start_index, i-1)
        elif (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i-1)
            current_word_start_index = i + 1


def reverse_characters(char_list, left, right):
    """ Reverses an array of characters in place

    Example:
    Input: ['ab', 'cd', 'ef', 'hi']
    Output: ['hi', 'ef', 'cd', 'ab']
    """
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

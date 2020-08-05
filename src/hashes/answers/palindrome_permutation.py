
def has_palindrome_permutation(string):
    count_set = set()
    for i in string:
        if i in count_set:
            count_set.remove(i)
        else:
            count_set.add(i)
    return len(count_set) <= 1


def solution(int_list):

    if len(int_list) < 3:
        raise Exception

    highest = max(int_list[0], int_list[1])
    lowest = min(int_list[0], int_list[1])
    highest_product_of_2 = int_list[0] * int_list[1]
    lowest_product_of_2 = int_list[0] * int_list[1]
    highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]

    for i in range(2, len(int_list)):
        current = int_list[i]
        highest_product_of_3 = max(highest_product_of_3,
                                   lowest_product_of_2 * current,
                                   highest_product_of_2 * current)
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * lowest,
                                  current * highest)
        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3

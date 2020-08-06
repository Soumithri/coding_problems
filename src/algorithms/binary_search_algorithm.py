"""
Start with the middle number: is it bigger or smaller than our target number?

Since the list is sorted, this tells us if the target would be in the left half
or the right half of our list.

We've effectively divided the problem in half. We can "rule out" the whole half
of the list that we know doesn't contain the target number.

Repeat the same approach (of starting in the middle) on the new half-size
problem. Then do it again and again, until we either find the number or
"rule out" the whole set.

Return True if element is present in input else return False

Examples:
num_list = [1, 2, 3, 4], target = 3, output = True
num_list = [1, 2, 3, 4], target = 5, output - False
"""


# def binary_search(target, num_list):
#     pass

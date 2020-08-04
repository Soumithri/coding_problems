
def merge_meeting(meetings):
    """ Given a collection of intervals, merge all overlapping intervals.

    Example 1:

    Input: [(1,3),(2,6),(8,10),(15,18)]
    Output: [(1,6),(8,10),(15,18)]
    Explanation: Since intervals (1,3) and (2,6) overlaps, 
                 merge them into (1,6).
    
    Example 2:

    Input: [(1,4),(4,5)]
    Output: [(1,5)]
    Explanation: Intervals (1,4) and (4,5) are considered overlapping.

    leetcode: https://leetcode.com/problems/merge-intervals/
    """

    sort_meetings = sorted(meetings, key=lambda x: x[0])
    result = [sort_meetings[0]]

    for i, j in sort_meetings[1:]:
        last_merge_start, last_merge_end = result[-1]
        if i <= last_merge_end:
            result[-1] = (last_merge_start, max(j, last_merge_end))
        else:
            result.append((i, j))
    return result


def merge_meeting(meetings):

    sort_meetings = sorted(meetings, key=lambda x: x[0])
    result = [sort_meetings[0]]

    for i, j in sort_meetings[1:]:
        last_merge_start, last_merge_end = result[-1]
        if i <= last_merge_end:
            result[-1] = (last_merge_start, max(j, last_merge_end))
        else:
            result.append((i, j))
    return result

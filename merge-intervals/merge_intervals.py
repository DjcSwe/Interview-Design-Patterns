def merge_intervals(intervals):
    if not intervals:
        return None

    result = [[intervals[0][0], intervals[0][1]]]

    for i in range(1, len(intervals)):
        # Last interval present in the output list
        last_added_interval = result[len(result) - 1]

        # Variables to store the start and end times of the current interval
        cur_start = intervals[i][0]
        cur_end = intervals[i][1]

        # The end time of the last interval present in the output list
        last_added_end = last_added_interval[1]

        # Overlapping condition
        if cur_start <= last_added_end:
            result[-1][1] = max(cur_end, last_added_end)
        # No overlap
        else:
            result.append([cur_start, cur_end])
    return result


# Driver code
def merge_intervals_test():
    all_intervals = [
        [[1, 5], [3, 7], [4, 6]],
        [[1, 5], [4, 6], [6, 8], [11, 15]],
        [[3, 7], [6, 8], [10, 12], [11, 15]],
        [[1, 5]],
        [[1, 9], [3, 8], [4, 4]],
        [[1, 2], [3, 4], [8, 8]],
        [[1, 5], [1, 3]],
        [[1, 5], [6, 9]],
        [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print("   Merged intervals:\t", result)
        print("-" * 100)
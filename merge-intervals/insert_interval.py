def insert_interval(existing_intervals, new_interval):
    # Read the starting and ending time of the new interval, into separate variables
    new_start, new_end = new_interval[0], new_interval[1]

    # Initialize variables to help in iterating over the existing intervals list
    i = 0
    n = len(existing_intervals)

    # Initialize an empty list to store the output
    output = []
    while i < n and existing_intervals[i][0] < new_start:
        output.append(existing_intervals[i])
        i = i + 1

    # If the new interval starts after the end of the last interval appended to the output list,
    # just append the new interval to the output list.
    if not output or output[-1][1] < new_start:
        output.append(new_interval)
    # Otherwise merge the two intervals
    else:
        # Copy any remaining intervals to the output list,
        output[-1][1] = max(output[-1][1], new_end)

    # similarly merging any overlaping intervals as we go
    while i < n:
        ei = existing_intervals[i]
        start, end = ei[0], ei[1]
        if output[-1][1] < start:
            output.append(ei)
        else:
            output[-1][1] = max(output[-1][1], end)
        i += 1
    return output


# Driver code
def insert_interval_test():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]

    for i in range(len(new_interval)):
        print(i + 1, ".\tExiting intervals: ", existing_intervals[i], sep="")
        print("\tNew interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print("\tUpdated intervals: ", output, sep="")
        print("-" * 100)
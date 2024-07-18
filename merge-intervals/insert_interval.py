def insert_interval(existing_intervals, new_interval):
    # Read the starting and ending time of the new interval, into separate variables
    new_start = new_interval[0]
    new_end = new_interval[1]

    # Initialize variables to help in iterating over the existing intervals list
    i = 0
    n = len(existing_intervals)

    # Initialize an empty list to store the output
    output = []

    # Add the intervals that start before the new interval.
    while i < n and existing_intervals[i][0] < new_start:
        output.append(existing_intervals[i])
        i = i + 1

    # If the new interval starts after the end of the last interval appended to the output list,
    # just append the new interval to the output list
    # if (output is empty) or (last-added-interval-end-time is less than new-interval-start-time)
    if not output or output[-1][1] < new_start:
        output.append(new_interval)

    # Otherwise merge the two intervals
    else:
        # Copy any remaining intervals to the output list
        # Last-added-interval-end-time is set to the maximum of (new-end-time or last-added-interval-end-time)
        output[-1][1] = max(output[-1][1], new_end)

    # similarly merging any overlapping intervals as we go
    # (remaining intervals to be added and merged)
    while i < n:
        remaining_interval = existing_intervals[i]
        start = remaining_interval[0]
        end = remaining_interval[1]

        # if (last-added-interval-end-time) is less than (current-remaining-interval-start-time)
        if output[-1][1] < start:
            output.append(remaining_interval)
        else:

            # set the last-added-interval-end-time to the maximum of its self or the remaining-interval-end-time
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
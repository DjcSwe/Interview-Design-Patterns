import heapq


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed

    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
            "(" + str(self.start) + ", " + str(self.end) + ")"


def employee_free_time(schedule):
    heap = []
    # Iterate for all employees' schedules
    # and add start of each schedule's first interval along with
    # its index value and a value 0.
    for i in range(len(schedule)):
        heap.append((schedule[i][0].start, i, 0))

    # Create heap from array elements.
    heapq.heapify(heap)

    # Take an empty array to store results.
    result = []

    # Set 'previous' to the start time of first interval in heap.
    previous = schedule[heap[0][1]][heap[0][2]].start

    # Iterate till heap is empty
    while heap:
        # Pop an element from heap and set value of i and j
        _, i, j = heapq.heappop(heap)

        # Select an interval
        interval = schedule[i][j]

        # If selected interval's start value is greater than the
        # previous value, it means that this interval is free.
        # So, add this interval (previous, interval's end value) into result.
        if interval.start > previous:
            result.append(Interval(previous, interval.start))

        # Update the previous as maximum of previous and interval's end value.
        previous = max(previous, interval.end)

        # If there is another interval in current employees' schedule,
        # push that into heap.
        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, (schedule[i][j + 1].start, i, j + 1))

    # When the heap is empty, return result.
    return result


# Function for displaying interval list
def display(vec):
    string = "["
    if vec:
        for i in range(len(vec)):
            string += str(vec[i])
            if i + 1 < len(vec):
                string += ", "
    string += "]"
    return string


# Driver code
def employee_free_time_test():
    inputs = [
        [[Interval(1, 2), Interval(5, 6)], [Interval(1, 3)], [Interval(4, 10)]],
        [[Interval(1, 3), Interval(6, 7)], [Interval(2, 4)], [Interval(2, 5), Interval(9, 12)]],
        [[Interval(2, 3), Interval(7, 9)], [Interval(1, 4), Interval(6, 7)]],
        [[Interval(3, 5), Interval(8, 10)], [Interval(4, 6), Interval(9, 12)], [Interval(5, 6), Interval(8, 10)]],
        [[Interval(1, 3), Interval(6, 9), Interval(10, 11)], [Interval(3, 4), Interval(7, 12)],
         [Interval(1, 3), Interval(7, 10)], [Interval(1, 4)], [Interval(7, 10), Interval(11, 12)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8)],
         [Interval(2, 3), Interval(4, 5), Interval(6, 8)]],
        [[Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)],
         [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)],
         [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)],
         [Interval(1, 2), Interval(3, 4), Interval(5, 6), Interval(7, 8), Interval(9, 10), Interval(11, 12)]]

    ]
    i = 1
    for schedule in inputs:
        print(i, '.\tEmployee Schedules:', sep="")
        for s in schedule:
            print("\t\t", display(s), sep="")
        print("\tEmployees' free time", display(employee_free_time(schedule)))
        print('-' * 100)
        i += 1

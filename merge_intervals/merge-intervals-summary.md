# Merge Intervals (Overview)
The merge intervals pattern deals with problems involving overlapping intervals. Each interval is represented by a
start and an end time. For example, an interval of `[10,20]` seconds means that the interval starts at `10` seconds and
ends at `20` seconds. This pattern involves tasks such as merging intersecting intervals, inserting new intervals into
existing sets, or determining the minimum number of intervals needed to cover a given range. The most common problems
solved using this pattern are event scheduling, resource allocation, and time slot consolidation.

### Does your problem match this pattern?
Yes, if both of these conditions are fulfilled:
* **Array of intervals:** The input data is an array of intervals.
* **Overlapping intervals:** The problem requires dealing with overlapping intervals, either to find their union,
their intersection, or the gaps between them.

### Real world problems.
* **Display busy schedule:** Display the busy hours of a user to other users without revealing the individual meeting 
slots in a calendar. 
* **Schedule a new meeting:** Add a new meeting to the tentative meeting schedule of a user in such a way that no two 
meetings overlap each other.
* **Task scheduling in operating systems (OS):** Schedule tasks for the OS based on task priority and the free slots in 
the machine’s processing schedule.

<br/>

## Merge Intervals
We are given an array of closed intervals, `intervals`, where each interval has a start time and an end time.
The input array is sorted with respect to the start times of each interval. For example, intervals =
`[ [1,4], [3,6], [7,9] ]` is sorted in terms of start times `1`, `3`, and `7`. <br/>
Your task is to merge the overlapping intervals and return a new output array consisting of only the non-overlapping
intervals.

### Solution
1. Insert the first interval from the input list into the output list.
2. Traverse the input list of intervals. For each interval in the input list, we do the following:
   * If the input interval is overlapping with the last interval in the output list, merge these two intervals and
   replace the last interval of the output list with this merged interval.
   * Otherwise, add the input interval to the output list.

### Time Complexity
The time complexity of this solution is *O*(*n*), where *n* is the number of intervals in the input list.

### Space Complexity
The space complexity of this solution is *O*(*1*), since we only use constant space other than the input and output
data structures.

<br />

## Insert Interval 
Given a sorted list of nonoverlapping intervals and a new interval, your task is to insert the new interval into the
correct position while ensuring that the resulting list of intervals remains sorted and nonoverlapping. Each interval
is a pair of nonnegative numbers, the first being the start time and the second being the end time of the interval.

### Solution 
1. Append all intervals occurring before the new interval to the output list until we find an interval that starts
after the starting point of the new interval.
2. If there is an overlap between the last interval in the output list and the new interval, merge them by updating
the end value of the last interval. Otherwise, append the new interval to the output list.
3. Continue iterating through the remaining intervals and merge the overlapping intervals with the last interval in 
the output list.
4. Return the final output list containing the merged intervals.

### Time Complexity
The time complexity is *O*(*n*), where *n* is the number of intervals in the input list.
This is because we iterate through the list once, checking and merging intervals as necessary.

### Space Complexity
The space complexity is *O*(1), since we only use constant space other than the input and output data structures.

<br />

## Interval List Intersections
For two lists of closed intervals given as input, `interval_list_a` and `interval_list_b`, where each interval has its 
own start and end time, write a function that returns the intersection of the two interval lists. <br />
For example, the intersection of [3,8] and [5,10] is [5,8]. 

### Solution
1. Set two pointers, `i` and `j`, at the beginning of both lists, respectively, for their iteration.
2. While iterating, find the latest starting time and the earliest ending time for each pair of
`intervals interval_list_a[i]` and `interval_list_b[j]` .
3. If the latest starting time is less than or equal to the earliest ending time, store it as an intersection.
4. Increment the pointer (`i` or `j`) of the list having the smaller end time of the current interval.
5. Keep iterating until either list is fully traversed.
6. Return the list of intersections.

### Time Complexity
The time complexity is *O*(*n* + *m*), where *n* and *m* are the number of meetings in `interval_list_a` and
`interval_list_b`, respectively.

### Space Complexity
The space complexity is *O*(1) as only a fixed amount of memory is consumed by a few temporary variables for
computations performed by the algorithm.
<br />

## Employee Free Time
You’re given a list containing the schedules of multiple employees. Each person’s schedule is a list of non-overlapping
intervals in a sorted order. An interval is specified with the start and end time, both being positive integers.
Your task is to find the list of finite intervals representing the free time for all the employees.

### Solution
We use the following variables in our solution:

- `previous`: Stores the end time of the previously processed interval.
- `i`: Stores the employee’s index value.
- `j`: Stores the interval’s index of the employee, i.
- `result`: Stores the free time intervals. <br/>

The steps of the algorithm are given below:

1. We store the start time of each employee’s first interval along with its index value and a value 0 into a min-heap.
2. We set `previous` to the start time of the first interval present in a heap.
3. Then we iterate a loop until the heap is empty, and in each iteration, we do the following:
   1. Pop an element from the min-heap and set `i` and `j` to the second and third values, respectively, from the
   popped value. 
   2. Select the interval from input located at `i, j`. 
   3. If the selected interval’s start time is greater than `previous`, it means that the time from `previous` to the
   selected interval’s start time is free. So, add this interval to the `result` array. 
   4. Now, update the `previous` as *max(previous, end time of selected interval).*
   5. If the current employee has any other interval, push it into the heap.
4. After all the iterations, when the heap becomes empty, return the `result` array.

### Time Complexity 
The time complexity of this algorithm is *O*(*mlog*(*n*)), where *n* is the number of employees and *m* is the total
number of intervals across all employees. This is because the time complexity of filling the heap is *O*(*nlog*(*n*)) 
and the time complexity of processing the heap is *O*(*mlog*(*n*)).

### Space Complexity
We use a heap in the solution, which can have a maximum of *n* elements. Hence, the space complexity of this solution
is *O*(*n*), where *n* is the number of employees.

<br/>

## Task Scheduler 
Given a character array tasks, where each character represents a unique task, and a positive integer n that represents
the cooling period between any two identical tasks, find the minimum number of time units the CPU will need to complete
all the given tasks. Each task requires one unit to perform, and the CPU must wait for at least n units of time before
it can repeat the same task. During the cooling period, the CPU may perform other tasks or remain idle.

### Solution
1. Store the frequency of each task and then sort them based on these frequencies. Begin by calculating the maximum
possible idle time given by: *(max frequency−1) × cooling period*. 
Here, *max frequency* refers to the highest frequency of any task in the sequence, and the *cooling period* is the 
specified interval between identical tasks. This formula represents the maximum time the CPU could potentially remain
idle between executions of tasks of the same type.
2. Next, iterate over the sorted task frequencies and update the idle time accordingly by subtracting the idle time
from the frequency of each task until the idle time becomes negative or all tasks have been processed. The adjustment
to the idle time during each iteration is calculated as: *idle time=idle time−min(max frequency−1,current frequency)*,
where *current frequency* represents the frequency of the task currently being processed.
3. Finally, return the total time required, which is the sum of the length of the task sequence and the computed idle
time, expressed as *length of tasks+idle time*. 

### Time Complexity
The time complexity of counting the frequencies of tasks is *O*(*n*), where *n* is the total number of tasks. 
Sorting the frequencies takes constant time *O*(1) due to the fixed size (26 for the 26 letters of the alphabet).
The proceeding steps also take constant time. Consequently, the overall time complexity of the solution is *O*(*n*). 

### Space Complexity
The space complexity is *O*(1) because it requires constant space to store task frequencies.

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
* **Display busy schedule:** Display the busy hours of a user to other users without revealing the individual meeting slots
in a calendar. 
* **Schedule a new meeting:** Add a new meeting to the tentative meeting schedule of a user in such a way that no two 
meetings overlap each other.
* **Task scheduling in operating systems (OS):** Schedule tasks for the OS based on task priority and the free slots in the
machine’s processing schedule.

<br/>

## Merge Intervals
We are given an array of closed intervals, intervals, where each interval has a start time and an end time.
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

### Time Complexity

### Space Complexity
# Sliding Window
The sliding window pattern is used to process sequential data, arrays, and
strings, for example, to efficiently solve subarray or substring problems.
It involves maintaining a dynamic window that slides through the array or 
string, adjusting its boundaries as needed to track relevant elements or 
characters. The window is used to slide over the data in chunks corresponding
to the window size, and this can be set according to the problem’s requirements.
It may be viewed as a variation of the two pointers pattern, with the pointers
being used to set the window bounds.

#### Does your problem match this pattern?
* **Contiguous data:** The input data is stored in a contiguous manner,
such as an array or string.
* **Processing subsets of elements:** The problem requires repeated 
computations on a contiguous subset of data elements (a subarray or a 
substring), such that the window moves across the input array from one end 
to the other. The size of the window may be fixed or variable, depending on the requirements of the problem.
* **Efficient computation time complexity:** The computations performed every 
time the window moves take constant or very small time.

<br/>

## Repeated DNA Sequences
Given a string, `s`, that represents a DNA subsequence, and a number `k`, 
return all the contiguous subsequences (substrings) of length `k` that occur 
more than once in the string. The order of the returned subsequences does not 
matter. If no repeated substring is found, the function should return an 
empty set.

### Solution
1. Iterate over all `k`-length substrings.
2. Compute the hash value for the contents of the window.
3. Add this hash value to the set that keeps track of the hashes of all 
substrings of the given length.
4. Move the window one step forward and compute the hash of the new window 
using the rolling hash method.
5. If the hash value of a window has already been seen, the sequence in this
window is repeated, so we add it to the output set.
6. Once all substrings have been evaluated, return the output set.

### Time Complexity
The average case time complexity of this solution is *O*(*n*), where n is the
length of the input string. 
* Time taken to populate the `nums` array: *O*(*n*).
* Time taken to traverse all the `k`-length substrings: *O*(*n* - 1 + *k*).
* Time taken to calculate the hash value of a `k`-length substring: *O*(1).
So, the dominating time complexity becomes *O*(*n*).

### Space Complexity
The space complexity of this solution is *O*(*n*).
* Space occupied by the `mapping` hash map: *O*(1).
* Space occupied by the `numbers` array: *O*(*n*).
* Space occupied by the `hash_set` set: *O*(*n* - *k* + 1).
So, the dominating space complexity becomes *O*(*n*)

<br/>

## Find Maximum in Sliding Window
Given an integer list, `nums`, find the maximum values in all the contiguous 
subarrays (windows) of size `w`.

### Solution
1. First, we check if the input list contains only one element. If it does, we 
directly return the input list because there is only one maximum element.
1. Then, we process the first `w` elements of the input list. We will use a 
deque to store the indexes of the candidate maximums of each window.
3. For each element, we perform the clean-up step, removing the indexes of the 
elements from the deque whose values are smaller than or equal to the value of 
the element we are about to add to the deque. Then, we append the index of the 
new element to the back of the deque.
4. After the first `w` elements have been processed, we append the element 
whose index is present at the front of the deque to the output list as it is 
the maximum in the first window.
5. After finding the maximum in the first window, we iterate over the remaining 
input list. For each element, we repeat Step 3 as we did for the first `w` 
elements.
6. Additionally, in each iteration, before appending the index of the current 
element to the deque, we check if the first index in the deque has fallen out 
of the current window. If so, we remove it from the deque.
7. Finally, we return the list containing the maximum elements of each window.

### Time Complexity
*O*(*n*)

### Space Complexity
The space compexity of this solution is *O*(*w*), where `w` is the window size.

<br />

## Minimum Window Subsequence
Given two strings, `str1` and `str2`, find the shortest substring in `str1`
such that `str2` is a subsequence of that substring.

### Solution
1. Initialize two indexes, `index_s1` and `index_s2`, to zero for iterating 
both strings.
2. If the character pointed by `index_s1` in `str1` is the same as the
character pointed by `index_s2` in `str2`, increment both pointers.
Otherwise, only increment `index_s1`.
3. Once `index_s2` reaches the end of `str2`, initialize two new indexes
(`start` and `end`). With these two indexes, we’ll slide the window backward.
4. Set `start` and `end` to `index_s1`.
5. If the characters pointed to by `index_s2` and `start` are the same,
decrement both of them. Otherwise, only decrement `start`.
6. Once, `str2` has been discovered in `str1` in the backward direction,
calculate the length of the substring.
7. If this length is less than the current minimum length, update the
`min_sub_len` variable and the `min_subsequence` string.
8. Resume the search in the forward direction from `start` + 1 in `str1`.
9. Repeat until `index_s1` reaches the end of `str1`.

### Time Complexity 
The outer loop iterates over the string str1, so the time complexity of this
loop will be *O*(*n*), where *n* is the length of string str1. Inside this loop,
there is a while loop that is used to iterate back over the window once all the
characters of str2 have been found in the current window. The time complexity
of this loop will be *O*(*m*), where *m* is the length of string str2.<br />
Therefore, the overall time complexity of this solution is *O*(*n* × *m*).

### Space Complexity 
Since we are not using any extra space apart from a few variables,
the space complexity is *O*(*n*).

<br />

## Longest Repeating Character Replacement
Given a string `s` and an integer `k`, find the length of the longest substring
in `s`, where all characters are identical, after replacing, at most, `k`
characters with any other lowercase English character.

### Solution
1. We iterate over the input string using two pointers.
2. In each iteration:
    1. If the new character is not present in the hash map, we add it. 
    Otherwise, we increment its frequency by 1.
    2. We slide the window one step forward if the number of replacements
    required in the current window has exceeded our limit.
    3. If the current window is the longest so far, then we update the length
    of the longest substring that has the same character.
3. Finally, we return the length of the longest substring with the same
character after replacements.

### Time Complexity 
The time complexity of the solution is *O*(*n*), where n is the length of the
input string because we iterate over the input string only once.

### Space Complexity 
The space complexity of the solution is *O*(1), since we will be storing the
frequency of *26* characters at most in the hash map.
 
<br />

## Minimum Window Substring
Given two strings, `s` and `t`, find the minimum window substring in `s`, 
which has the following properties:
1. It is the shortest substring of `s` that includes all of the characters
present in `t`.
2. It must contain at least the same frequency of each character as in `t`.
3. The order of the characters does not matter here.

### Solution
1. We validate the inputs. If `t` is an empty string, we return an empty string.
2. Next, we initialize two hash maps: `req_count`, to save the frequency of
characters in `t`, and `window`, to keep track of the frequency of characters
of `t` in the current window. We also initialize a variable, `required`,
to hold the number of unique characters in `t`. Lastly, we initialize `current`
which keeps track of the characters that occur in `t` whose frequency in the
current window is equal to or greater than their corresponding frequency in `t`.
3. Then, we iterate over `s` and in each iteration we perform the following
steps:
    1. If the current character occurs in `t`, we update its frequency in the
    `window` hash map.
    2. If the frequency of the new character is equal to its frequency in
    `req_count`, we increment current.
    3. If `current` is equal to `required`, we decrease the size of the window
    from the start. As long as `current` and required are equal, we decrease
    the window size one character at a time, while also updating the minimum
    window substring. Once `current` falls below `required`, we slide the right
    edge of the window forward and move on to the next iteration. 
4. Finally, when `s` has been traversed completely, we return the minimum window substring.

### Time Complexity
the time complexity for the solution is *O*(*n* + *m*), where *n* and *m* are
the lengths of the strings `s` and `t`. In the worst case, each hash map
operation will cost *O*(*m*). <br />
Hence, the overall time complexity would be 
*O*(*m* + (*n* x *m*))

### Space Complexity
Since the characters in `t` are limited to uppercase and lowercase English
letters, there is a maximum of 52 possible characters. Therefore, the size of
the `req_count` and `window` hash maps will be at most 52, regardless of the
length of `t`. <br />
Therefore, the space complexity of this solution will be *O*(1).

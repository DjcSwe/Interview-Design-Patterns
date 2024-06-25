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


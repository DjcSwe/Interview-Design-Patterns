# Two Pointers
The **two pointers** pattern is a versatile technique used in problem-solving to efficiently traverse or manipulate
sequential data structures, such as arrays or linked lists. As the name suggests, it involves maintaining two pointers
that traverse the data structure in a coordinated manner, typically starting from different positions or moving in 
opposite directions. These pointers dynamically adjust based on specific conditions or criteria. Whenever there’s a
requirement to find two data elements in an array that satisfy a certain condition, the two pointers pattern should
be the first strategy to come to mind.

#### Does your problem match this pattern?
Yes, if all of these conditions are fulfilled:
* **Linear data structure:** The input data can be traversed in a linear fashion, such as an array, linked list,
or string.
* **Process pairs:** Process data elements at two different positions simultaneously.
* **Dynamic pointer movement:** Both pointers move independently of each other according to certain conditions or
criteria. In addition, both pointers might move along the same or two different data structures.

<br />

## Valid Palindrome
Write a function that takes a string, `s`, as an input and determines whether or not it is a palindrome.

### Solution
* Initialize two pointers and move them from opposite ends.
* The first pointer starts at the beginning of the string and moves toward the middle, while the second pointer
starts at the end and moves toward the middle.
* Compare the elements at each position to detect a nonmatching pair.
* If both pointers reach the middle of the string without encountering a nonmatching pair, the string is a palindrome.

### Time Complexity
The time complexity is *O*(*n*), where *n* is the number of characters in the string. However, our algorithm will only
run (*n*/2) times, since two pointers are traversing toward each other.

### Space Complexity
The space complexity is *O*(1), since we use constant space to store two indexes.

<br />

## Sum of Three Values
Given an array of integers, `nums`, and an integer value, `target`, determine if there are any three integers in `nums`
whose sum is equal to the `target`, that is, `nums[i] + nums[j] + nums[k] == target`.
Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

### Solution
First, sort the array in ascending order. To find a triplet whose sum is equal to the target value, loop through the
entire array. In each iteration:
1. Store the current array element and set up two pointers (`low` and `high`) to find the other two elements that
complete the required triplet.
    1. The `low` pointer is set to the current loop’s index + 1.
    2. The `high` is set to the last index of the array.
2. Calculate the sum of array elements pointed to by the current loop’s index and the `low` and `high` pointers.
3. If the sum is equal to `target`, return TRUE.
4. If the sum is less than `target`, move the `low` pointer forward.
5. If the sum is greater than `target`, move the `high` pointer backward.

### Time Complexity
In the solution above, sorting the array takes *O*(*nlog*(*n*)) and the nested loop takes *O*(*n<sup>2<sup />*) to find
the triplet. Here, *n* is the number of elements in the input array. Therefore, the total time complexity of this
solution is *O*(*nlog*(*n*) + *n<sup>2<sup />*), which simplifies to O(*n<sup>2<sup />*).

### Space Complexity
Because we use the build-in Python `sort()` function, the space complexity is *O*(*n*).

<br />

## Remove n<sup>th</sup> Node from End of List
Given a singly linked list, remove the n<sup>th</sup> node from the end of the list and return its head.

### Solution
1. Two pointers, `right` and `left`, are set at the head node.
2. Move the `right` pointer `n` steps forward.
3. If `right` reaches NULL, return `head`'s next node.
4. Move both `right` and `left` pointers forward till `right` reaches the last node.
5. Relink the `left` node to the node at `left`'s next to the next node.
6. Return `head`.

### Time Complexity
The time complexity is *O*(*n*), where `n` is the number of nodes in the linked list.

### Space Complexity
The space complexity is *O*(1) because we use constant space to store two pointers.

<br />

## Sort Colors
Given an array, colors, which contains a combination of the following three elements:
* `0` (representing red)
* `1` (representing white)
* `2` (representing blue) <br />

Sort the array in place so that the elements of the same color are adjacent, with the colors in the order of red,
white, and blue. To improve your problem-solving skills, do not utilize the built-in sort function.

### Solution
1. Traverse the array and swap elements, as required, to organize them correctly.
2. If the encountered color is red, swap its value with that of the `start` pointer. If the color is blue, 
swap its value with that of the end pointer.
3. White elements are skipped, and pointers are adjusted accordingly.
4. The array is sorted when the `end` pointer moves to the left of the `current` pointer.

### Time Complexity
The time compolexity of this solution is *O*(*n*) since we're only traversing the array once. 

### Space Complexity
The space complexity of this solution is *O*(1) since no extra space is used.

<br />

## Reverse Words in a String
Given a sentence, reverse the order of its words without affecting the order of letters within the given word. 

### Solution
1. **Reversing the entire sentence:**
   * We first reverse the complete string. This step places the words in their correct positions relative to
   each other, although each word is backward.
2. **Reversing each word:**
   * Iterate through the reversed sentence:
       1. Use two pointers, `start` and `end`, both initially set to 0. The first pointer, `start`, marks the beginning 
       of a word, and the second pointer, `end`, finds the end of a word.
       2. When the end of a word is found (either a space or the end of the string), we reverse the characters in that
       word in place.
       3. After reversing, we update `start` to point to the beginning of the next word.
       4. Now, we'll repeat this process for the next word. At the end of all iterations, we get the reversed words in
       the string.
       5. We repeat this process for all words in the string.

### Time Complexity
It takes *O*(*n*) time to remove the leading and trailing whitespace and replace multiple spaces with a single space in
the sentence, where *n* is the length of the sentence. Additionally, the array is traversed twice in
*O*(*n* + *n*) = *O*(*n*)time. Therefore, the overall time complexity of this solution is *O*(*n*).

### Space Complexity
The space complexity of this solution is *O*(*n*), since, at the start of the algorithm, we copy it into a list of
characters to overcome the issue of strings being immutable in Python.

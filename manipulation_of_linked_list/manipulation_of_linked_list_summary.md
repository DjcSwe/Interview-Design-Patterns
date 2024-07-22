# In-Place Manipulation of a Linked List
The in-place manipulation of a linked list pattern allows us to modify a linked list without using any additional
memory. In-place refers to an algorithm that processes or modifies a data structure using only the existing memory
space, without requiring additional memory proportional to the input size. This pattern is best suited where we need to
modify the structure of the linked list. <br />
The naive approach to reverse a linked list is to traverse it and produce a new linked list with every linked reversed.
The time complexity would be O(n) while consuming O(n) extra space. <br />
An optimized solution would be to iterate over the linked list while keeping track of three nodes: `the current node`,
`the next node`, and `the previous node`. Keeping track of these three nodes enables reversal efficiency for every link
between every node. The in-place reversal solution works in O(n) time and consumes O(1) space.

### Does your problem match this pattern?
Yes, if both of these conditions are fulfilled:
* **Linked list restructuring:** The input data is given as a linked list, and the task is to modify its structure
without modifying the data of the individual nodes.
* **In-place modification:** The modifications to the linked list must be made in place, that is, we’re not allowed to
use more than O(1) additional space.

### Real-world problems
* **File system management:** File systems often use linked lists to manage directories and files. Operations such as
rearranging files within a directory can be implemented by manipulating the underlying linked list in place.
* **Memory management:** In low-level programming or embedded systems, dynamic memory allocation and deallocation often
involve manipulating linked lists of free memory blocks. Operations such as merging adjacent free blocks or splitting]
large blocks can be implemented in place to optimize memory usage.

<br />


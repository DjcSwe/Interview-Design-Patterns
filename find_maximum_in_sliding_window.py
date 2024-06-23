from collections import deque


def clean_up(i, current_w, nums):
    while current_w and nums[i] >= nums[current_w[-1]]:
        current_w.pop()


def find_max_sliding_window(nums, w):
    if len(nums) == 1:
        return nums

    max_list = []
    current_w = deque()

    # iterate over the first w elements
    for i in range(w):
        clean_up(i, current_w, nums)
        current_w.append(i)

    # first element is always the max
    max_list.append(nums[current_w[0]])

    # iterate over remaining windows
    for i in range(w, len(nums)):
        clean_up(i, current_w, nums)
        if current_w and current_w[0] <= (i - w):
            current_w.popleft()
        current_w.append(i)
        max_list.append(nums[current_w[0]])

    return max_list


def find_max_sliding_window_test():
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 6]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput list:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

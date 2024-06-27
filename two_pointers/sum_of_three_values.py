def find_sum_of_three(nums, target):
    nums.sort()
    for i in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            if nums[i] + nums[low] + nums[high] == target:
                return True
            if nums[i] + nums[low] + nums[high] < target:
                low += 1
            if nums[i] + nums[low] + nums[high] > target:
                high -= 1
    return False

def find_sum_of_three_test():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)
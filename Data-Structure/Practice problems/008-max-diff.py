# Find Maximum Difference Between Two Consecutive Elements (Brute Force Approach)

# You are given a list of integers. Write a Python program to find the maximum difference between two consecutive elements in the list using a brute-force approach. The difference is defined as the absolute value of the difference between two consecutive elements.

def find_max_diff(numbers):
    """Find maximum difference between consecutive elements"""
    if len(numbers) < 2:
        return 0

    max_diff = 0
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff > max_diff:
            max_diff = diff
    print(max_diff)             # 7
    # return max_diff

lst = [1, 7, 3, 10, 5]
find_max_diff(lst)
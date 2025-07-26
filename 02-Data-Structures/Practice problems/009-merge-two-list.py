# Merge Two Sorted Lists
# You are given two sorted lists of integers. Write a Python function to merge these two sorted lists into one sorted list. The resulting list should also be in non-decreasing order.

def merge_list_inbuilt(list1, list2):
    """Merge two sorted lists into one sorted list"""
    return sorted(list1 + list2)


list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged_list = merge_list_inbuilt(list1, list2)
print(merged_list)
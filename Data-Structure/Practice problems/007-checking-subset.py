# Check if a List is a Subset of Another List (Brute Force Approach)

# You are given two lists of integers. Write a Python program that checks whether the first list is a subset of the second list using a brute-force approach, without using the in keyword. A list is considered a subset if all elements of the first list are present in the second list.

def check_subset(list1, list2):
    """Check if list1 is a subset of list2 using brute force"""
    for element in list1:
        found = False
        for item in list2:
            if element == item:
                found = True
                break
        if not found:
            return False
    return True

lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]

result = check_subset(lst1, lst2)
print(result)

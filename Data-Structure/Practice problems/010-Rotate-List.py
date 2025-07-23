# Rotate a List (Without Slicing)
# You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

# Parameters:
# lst (List of integers): The list to be rotated.
# k (Integer): The number of positions to rotate the list.

# Example:
# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

def rotate_list(numbers, k):
    """Rotates a list to the right by k positions"""
    for _ in range(k):
        element = numbers.pop()
        numbers.insert(0, element)
    return numbers


lst = [1, 2, 3, 4, 5]
k = 2
print(f"Original: {lst}")
print(f"Rotated by {k}: {rotate_list(lst, k)}")
# Output: [4, 5, 1, 2, 3]

lst2 = [10, 20, 30, 40, 50]
k2 = 3
print(f"Original: {lst2}")
print(f"Rotated by {k2}: {rotate_list(lst2, k2)}")
# Output: [30, 40, 50, 10, 20]

# Write a python function that calculates the sum of all elements in a given list of integers.

# Parameters:
# numbers (List of integers): The input list containing integers.

# Returns:
# An integer representing the sum of all elements in the input list.

# Example:
# Input: numbers = [1, 2, 3, 4, 5]
# Output: 15

def list_sum(numbers):
    """Returns the sum of a list"""
    sum = 0
    for number in numbers:
        sum += number
    return sum


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
result = list_sum(numbers_list)
print(result)
# Write a Python function that finds and returns the largest element in a given list of integers.

def largest(numbers):
    """Finds the largest number in a list"""
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = [3, 8, 2, 10, 5]
print(largest(numbers)) # 10

numbers2 = [-5, -10, -2, -1, -7]
print(largest(numbers2)) # -1
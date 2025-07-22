# Check if All Elements in a List are Unique

# You are given a list of integers. Write a Python program that checks if all elements in the list are unique. If all elements are unique, return True; otherwise, return False.

def check_uniqueness(numbers):
    """Checks if the list is unique or has duplicate values"""
    no_duplicate = []
    for number in numbers:
        if number in no_duplicate:
            return False
        else:
            no_duplicate.append(number)
    return True


# Calling the function
print(check_uniqueness([1, 2, 3, 4, 5]))    # True
print(check_uniqueness([1, 2, 3, 4, 4, 5])) # False
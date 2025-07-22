# Remove Duplicates from a List

# You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

def remove_duplicate(numbers):
    """Returns a list without duplicate values"""
    no_dup_numbers = []
    for number in numbers:
        if number not in no_dup_numbers:
            no_dup_numbers.append(number)
    return no_dup_numbers

def remove_dupli_with_sets(numbers):
    """Returns a list witout duplicate values"""
    numbers_set = set(numbers)
    numbers = list(numbers_set)
    return numbers

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicate(lst))
print(remove_dupli_with_sets(lst))
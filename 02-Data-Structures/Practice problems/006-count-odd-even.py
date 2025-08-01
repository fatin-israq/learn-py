# Count Even and Odd Numbers in a List
# You are given a list of integers. Write a Python program that counts and returns the number of even and odd numbers in the list.

# Parameters:
# lst (List of integers): The list of integers where you will count the even and odd numbers.

# Returns:
# A tuple (even_count, odd_count) where even_count is the number of even numbers and odd_count is the number of odd numbers.

def count_even_odd(numbers):
    even = 0 
    odd = 0
    for number in numbers:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return (even, odd)

lst = [1, 2, 3, 4, 5]
print(count_even_odd(lst))
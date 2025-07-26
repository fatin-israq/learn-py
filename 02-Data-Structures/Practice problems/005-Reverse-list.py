# Reverse a List (Non-Slicing Approach)

# You are given a list of integers. Write a Python program that reverses the list without using slicing (lst[::-1]). The program should return the reversed list.

def reverse_list(numbers):
    reverse = []
    for i in range(len(numbers)):
        reverse.append(numbers.pop())
    return reverse

lst = [1, 2, 3, 4, 5]
print(f"List = {lst}")
print(f"Reversed List = {reverse_list(lst)}")
# Check if Tuple is Palindromic
# Design a Python function named is_palindromic_tuple to check if a tuple is palindromic, meaning it reads the same forwards and backwards.

def is_palindromic_tuple(tup):
    # Edge case: Empty tuple or single element tuple means palindrome
    if len(tup) <= 1:
        return True
    
    # Check each element against its corresponding element from the end
    for i in range(len(tup)//2):
        left_element = tup[i]                       # Element from start
        right_element = tup[len(tup) - i - 1]       # Corresponding element from end
        # If elements don't match, not a palindrome
        if left_element != right_element:
            return False
    # All coresponding elements matched - it's a palindrome
    return True

tup1 = ('a', 'b', 'c', 'b', 'a')
print(is_palindromic_tuple(tup1))

tup2 = (1, 2, 3, 4, 5)
print(is_palindromic_tuple(tup2))
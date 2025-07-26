# Merge Three Dictionaries
# Design a Python function named merge_three_dictionaries to merge exactly three dictionaries into one.

def merge_three_dictionaries(dict1, dict2, dict3):
    """Returns a dictionary merged from three dictionaries"""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = value

    for key, value in dict3.items():
        merged_dict[key] = value
    
    return merged_dict


dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

merged_dict = merge_three_dictionaries(dict1, dict2, dict3)
print(merged_dict)
# Merge Lists to Dictionary
# Design a Python function named merge_lists_to_dictionary to merge two lists into a dictionary where elements from the first list act as keys and elements from the second list act as values.

# Parameters:
# keys (List): A list of keys.
# values (List): A list of values.

def merge_list(keys, values):
    """Merging two lists into one dictionary,
    where one list is considered as key,
    another one as value"""
    dicts = dict()
    for key, value in zip(keys, values):
        dicts[key] = value
    return dicts

keys = ['a', 'b', 'c']
values = [1, 2, 3]

merged_dict = merge_list(keys, values)
print(merged_dict)
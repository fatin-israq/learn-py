# Merge Dictionaries with Overlapping Keys
# Design a Python function named merge_dicts_with_overlapping_keys that merges multiple dictionaries into a single dictionary. If a key appears in more than one dictionary, sum up their values.

def merge_dicts_with_overlapping_keys(dictionaries):
    # initialize an empty dict to store the merged dictionary
    merged_dict = {}
    for dictionary in dictionaries:
        # iterate through each key-value pair in one dictionary
        for key, value in dictionary.items():
            # check if this key already exists
            if key not in merged_dict:
                # first time seeing this key - add key to dict
                merged_dict[key] = value
            else:
                # key already exists - add the current value 
                merged_dict[key] += value
    return merged_dict

# Test data
dictionaries = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
print(merge_dicts_with_overlapping_keys(dictionaries))
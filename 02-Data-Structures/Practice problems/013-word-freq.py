# Count Word Frequency
# Design a Python function named count_word_frequency to count the frequency of words in a sentence and store the counts in a dictionary.

def count_word_frequency(string):
    """Returns a dictionary with counted words"""

    # initialize an empty dictionary to store word frequencies
    words = dict()

    # Iterate each words
    for word in string.split():
        # If word is not in the dictionary, add it with a count of 1
        if word not in words:
            words[word] = 1
        # If word is already in the dictionary, increment its count
        else:
            words[word] += 1
    return words

str = "the quick brown fox jumps over the lazy dog"
print(count_word_frequency(str))
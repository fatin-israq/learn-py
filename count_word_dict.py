# Question: Write a function that takes a sentence as input and returns a dictionary 
# where each word is a key and its frequency (count) in the sentence is the value.

def count_word (sentence):
    word_list = sentence.split()
    word_dict = {}

    for w in word_list:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    print(word_dict)


count_word ("Something is better than Nothing, Something is better")
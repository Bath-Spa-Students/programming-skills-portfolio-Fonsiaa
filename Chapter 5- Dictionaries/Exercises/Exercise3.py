#key = values
dict = {'mutables' : 'values are changable',
        'positive_indexing' : 'the first number in the list starts with zero', 
        'negative_indexing' : 'starts from the right and starts with negative one',
        'repetition_list' : 'repeats the list the',
        'comment' : 'using the # to make notes',
        'float' : 'a decimal number',
        'integer' : 'a whole number'} 

for word, definition in dict.items():
    print(f"\n{word.title()}:{definition}")
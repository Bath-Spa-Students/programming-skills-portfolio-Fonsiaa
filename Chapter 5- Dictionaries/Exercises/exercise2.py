#key : values
#the terminology I've learned
dict = {'mutables' : 'values are changeable',
        'positive_indexing' : 'the first number in the list starts with zero', 
        'negative_indexing' : 'starts from the right and starts with negative one',
        'repetition_list' : 'repeats the list the',
        'comment' : 'using the # to make notes'} 

#using the f-string
word = 'mutables'
print(f"\n{word.title()}:{dict[word]}")
word = 'positive_indexing'
print(f"\n{word.title()}:{dict[word]}")
word = 'negative_indexing'
print(f"\n{word.title()}:{dict[word]}")
word = 'repetition_list'
print(f"\n{word.title()}:{dict[word]}")
word = 'comment'
print(f"\n{word.title()}:{dict[word]}")

def make_shirt(size, message):
    """Summarizing the size of the t-shirt."""#commenting
    print(f"\nI'm going to make a {size} t-shirt.")#using the f-string
    print(f'Printed on the t-shirt is: {message}')

#print on the t-shirt and the t-shirt size
make_shirt('large', 'I love Python!')#using a key argument
make_shirt(message="Earth loves you.", size='medium')#positional argument

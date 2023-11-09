#using the define function
def make_shirt(size, message):
    """Summarize the shirt that's going to be made."""#commenting
    print(f"\nI'm going to make a {size} t-shirt.")#f-string
    print(f'Printed on the t-shirt is:"{message}"')

make_shirt('large', 'I luv Python!')#keyword argument
make_shirt(message="I luv Python!.", size='medium')#positional argument
make_shirt(message="Earth loves you.", size='small')#positional argument

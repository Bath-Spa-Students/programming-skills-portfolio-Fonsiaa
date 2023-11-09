message = "\nWhat more toppings on your pizza? or enter 'quit': "

#using the if-else statement
while True:
    topping = input(message)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break #will break the loop
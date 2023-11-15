message = "\nWhat more toppings do you want on your pizza? or 'no': "

#using the if-else statement
while True:
    topping = input(message)
    if topping != 'no':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break #will break the loop

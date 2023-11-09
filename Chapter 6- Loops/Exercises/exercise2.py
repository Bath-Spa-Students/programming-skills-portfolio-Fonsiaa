prompt = "May I know your age?"
prompt += "\nor enter 'quit'. "

#using booleans
while True:
    age = input(prompt) #takes the users age
    if age == 'quit':
        break #stops the loop
    age = int(age)
    
    if age < 3:
        print("  Your ticket is free!")
    elif age < 13:
        print("  Your ticket costs $10.")
    else:
        print("  Your ticket costs $15.")
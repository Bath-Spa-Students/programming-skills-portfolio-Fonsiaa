sandwich_orders = ['Cucumber tea', 'Grilled cheese', 'Mayonnaise tuna'] #list
finished_sandwiches = []

#using the f-string
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm still making your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich) #prints the finished_sandwiches list

#using the f-string
print("\n")
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} sandwich has been made.")
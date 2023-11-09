sandwich_orders = ['pastrami', 'Cucumber tea', 'Grilled cheese', 
                'pastrami','Mayonnaise tuna', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami') #removes the item from the list

print("\n") #adds a new line
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm still working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n") #adds a newline
for sandwich in finished_sandwiches:
    print(f"Your {sandwich} sandwich has been made.")
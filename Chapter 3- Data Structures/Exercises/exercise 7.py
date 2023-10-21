#Uses the positive indexing
guests = ["Sheila" , "Juluis" , "Charles"]
#Sheila = 0
#Juluis = 1
#Charles = 2

#string format () formula
for guest in guests:
    print ("Good day {}, I would like to invite you to dinner.".format(guest))
print()

print("{} cannot make it to the dinner." .format(guests[2]))
#replacing the person who cannot make it to dinner
guests.pop(2)
print()

#The person who will replace Charles
#Making Tobi = 2
guests.append("Tobi")
for guest in guests:
    print("Good day {}, I would like to invite you to dinner.".format(guest))
print()

#Invitng more people to dinner
print("I have invited more guest to dinner")
print()

#The invited people
guests.insert(0, "Estrilta")
#Estrilta will be the first guest in the list
#Estrilta = 0
guests.insert(4,"Roger")
#Roger will the last guest in the list
#Roger = 4

#Update guests list:
#Estrilta = 0
#Sheila = 1
#Juluis = 2
#Tobi = 3
#Roger = 4

for guest in guests:
    print("Good day {}, I would like to invite you to dinner.".format(guest))
print()
print("Sorry, I can invite only two people")

guests.pop(0)
print("Until next time, Estrilta")
#Update guests list:
#Sheila = 0
#Juluis = 1
#Tobi = 2
#Roger = 3

guests.pop(3)
print("Until next time, Roger")
#Update guests list:
#Sheila = 0
#Juluis = 1
#Tobi = 2

guests.pop(2)
print("Later, Tobi")
#Update guests list:
#Sheila = 0
#Juluis = 1

print("{0} & {1}, you are still invited to dinner.".format(guests[0], guests[1]))
#Uses the positive indexing
guests = ["Sheila" , "Juluis" , "Charles"]
#string format () formula
for guest in guests:
    print ("Good day {}, I would like to invite you to dinner.".format(guest))
print()
print("{} cannot make it to the dinner." .format(guests[2]))
#replacing the person who cannot make it to dinner
guests.pop(2)
print()
#The person who will replace Charles
guests.append("Tobi")
for guest in guests:
    print("Good day {}, I would like to invite you to dinner.".format(guest))

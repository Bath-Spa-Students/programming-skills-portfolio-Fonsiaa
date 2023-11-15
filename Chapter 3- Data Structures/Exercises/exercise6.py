msg = "Sorry, I can only invite 2 people"
#Uses the positive indexing
guests = ["Toro" , "Luffy" , "Lily" , "Tobi"]
#string format () formula
for guest in guests:
    print ("Good day {}, I would like to invite you to dinner.".format(guest))
print()
print("Sorry {}, I can only invite two people for dinner." .format(guests[0]))
#replacing the person who cannot make it to dinner
del guests [0]
print()
print("Sorry {}, I can only invite two people for dinner." .format(guests[1]))
#replacing the person who cannot make it to dinner
del guests [1]
print()

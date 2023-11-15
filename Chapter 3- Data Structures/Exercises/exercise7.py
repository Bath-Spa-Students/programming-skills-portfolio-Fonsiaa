#encoding a list
places = ["France" , "Venice" , "Singapore" , "Doha" , "England"]

print("Original order:")#order doesn't change
print(places)

print("\nAlphabetical:")#orders it from a to z
print(sorted(places))

print("\nOriginal order:")#prints the original
print(places)

print("\nReverse alphabetical:")#orders from z to a
print(sorted(places, reverse=True))

print("\nOriginal order:")
print(places)

print("\nReversed:")
places.reverse()
print(places)

print("\nOriginal order:")
places.reverse()
print(places)

print("\nAlphabetical")
places.sort()
print(places)

print("\nReverse alphabetical")
places.sort(reverse=True)
print(places)

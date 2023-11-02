pets= []

# inputting the details of the pet
pet = {'gender' : 'female',
    'mammal': 'dog',
    'name': 'Lasso',
    'owner': 'Geli',
    'age': '2 years old',
    'eats': 'tuna',}
pets.append(pet)

pet = {'gender' : 'male',
    'Amphibians': 'toad',
    'name': 'Pod',
    'owner': 'Tiff',
    'age': '6 years old',
    'eats': 'worms',}
pets.append(pet)

#information of the pet
for pet in pets:
    print(f"Information of {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
#rivers and their specific country
rivers = {
    'Amazon': 'Brazil',
    'Yangtze' : 'China',
    'Orange' : 'South Africa'}


for river, country in rivers.items():
    print(f"The {river} flows through {country()}.")

print("\nThe following are rivers:")
for river in rivers.keys():
    print(f"- {river()}")

print("\nCountries with river:")
for country in rivers.values():
    print(f"- {country()}")
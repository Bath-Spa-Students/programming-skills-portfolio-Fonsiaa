def city_country(city, country):
    """Return a string like 'Santiago, Chile'.""" #commenting
    #using the f-string
    return f"{city.title()}, {country.title()}" #function ends

city = city_country('Copenhagen', 'Denmark')
print(city)#prints the values

city = city_country('Toronto', 'Canada')
print(city)

city = city_country('Singapore', 'Republic of Singapore')
print(city)
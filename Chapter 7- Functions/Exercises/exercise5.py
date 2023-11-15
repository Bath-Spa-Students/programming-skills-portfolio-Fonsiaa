def city_country(city, country):
    """Return a string like 'Santiago, Chile'.""" #commenting
    #using the f-string
    return f"{city.title()}, {country.title()}"
city = city_country('Copenhagen', 'Denmark')
print(city)#prints the values

city = city_country('Toronto', 'Canada')
print(city)#assigning the value to the caller

city = city_country('Singapore', 'Republic of Singapore')
print(city)

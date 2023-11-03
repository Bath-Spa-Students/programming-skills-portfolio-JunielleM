#Print and loop the major rivers
dictionary ={
    'Yangtze': 'China',
    'Amazon': 'Peru',
    'Mississippi-Missouri': 'United States'
}
for dictionary, country in dictionary.items():
    print(f"This {dictionary} river is in {country}")

dictionary = {
    'Yangtze': 'China',
    'Amazon': 'Peru',
    'Mississippi-Missouri': 'United States'
}

# Loop to print the name of each river
print("Rivers:")
for river in dictionary.keys():
    print(river)

countries_river = ["China", "Peru", "United States"]

# Print country then for loop
print("\nCountries:")
for country in countries_river:
    print(country)


n = int(input())
arr = [input() for i in range(n)]
country_set = set(arr)
number_of_countries = len(country_set)
print(country_set)
print(number_of_countries)
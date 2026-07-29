# ## 💻 Exercises: Day 14

# ```py
# countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ```

# ### Exercises: Level 1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1. Explain the difference between map, filter, and reduce.
# 2. Explain the difference between higher order function, closure and decorator
# 3. Define a call function before map, filter or reduce, see examples.
# 4. Use for loop to print each country in the countries list.
print(", ".join(countries))

# 5. Use for to print each name in the names list.
print(", ".join(names))
# 6. Use for to print each number in the numbers list.
print(", ".join(map(str, numbers)))

# ### Exercises: Level 2

# 1. Use map to create a new list by changing each country to uppercase in the countries list
def upper_case(name):
    return name.upper()

is_upper_case = map(upper_case, names)
print(list(is_upper_case))

# 1. Use map to create a new list by changing each number to its square in the numbers list

def squared(s):
    return s**2

square = map(squared, numbers)
print(list(square))
# 1. Use map to change each name to uppercase in the names list

# 1. Use filter to filter out countries containing 'land'.
def land_name(country):
    if 'land' in country:
        return True

country_land = filter(land_name, countries)
print(list(country_land))

# 1. Use filter to filter out countries having exactly six characters.
def six(country):
    if len(country) == 6:
        return True

six_c = filter(six, countries)
print(list(six_c))
# 1. Use filter to filter out countries containing six letters and more in the country list.
def moresix(country):
    if len(country) >= 6:
        return True

more_six_c = filter(moresix, countries)
print(list(more_six_c))
# 1. Use filter to filter out countries starting with an 'E'
def start_e(country):
    if country.startswith('E'):
        return True
s_e = filter(start_e, countries)
print(list(s_e))
# 1. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# 1. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def string_list(s):
    return isinstance(s, str)

arr = [1, 'shrestha' , 9, 'sneha' , 45.0]
ans = filter(string_list, arr )
print(list(ans))
# 1. Use reduce to sum all the numbers in the numbers list.
from functools import reduce
def sum_num(sum_u, num):
    return sum_u + num
  
sum_of_num = reduce(sum_num, numbers)
print(sum_of_num)
# 1. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

# 1. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# 1. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# 2. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# 1. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# ### Exercises: Level 3

# 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
#    - Sort countries by name, by capital, by population
#    - Sort out the ten most spoken languages by location.
#    - Sort out the ten most populated countries.
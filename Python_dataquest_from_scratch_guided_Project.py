# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:00:22 2017

@author: bEgbedokun
"""

cities = []
cities.append("Albuquerque")
cities.append(749)
cities.append("Anaheim")
cities.append(371)

print(cities)


cities = []
crime_rate = []

cities.append("Albuquerque")
cities.append("Anaheim")
cities.append("Anchorage")
cities.append("Arlington")
cities.append("Atlanta")

crime_rate.append(749)
crime_rate.append(371)
crime_rate.append(828)
crime_rate.append(503)
crime_rate.append(1379)

print(cities, crime_rate)

for i in range(5):
    print(i)


cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

ending_index = len(cities)
ending_index1 = len(crime_rates)

cities_slice = cities[2:ending_index]
cr_slice = crime_rates[3:ending_index1]

print(cities_slice, cr_slice)


 #We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

 #Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

 #Code from previous cells
#f = open('crime_rates.csv', 'r')
#data = f.read()
#
#rows = data.split('\n')
#first_five_element = rows[0:5]
#print(first_five_element)
#

#Here are the things you need to include in each of these components:

#for Loop

#Syntax - the words for and in need to be included in the statement
#Iterator variable - the variable name you decide to use to refer to
# each element in the list (city)
#Sequence - the variable you want to iterate over (cities)
#Colon - loop statements must end with a colon (:)
#Loop Body

#Indentation - every line of code within the loop should be indented four spaces
#Logic - the actual code we want to execute for each element. In the above code
# block, for example, we update the iterator variable (city) in each iteration
# of the loop.


rows = ['ee', 'ss', 'ee', 'eee', 'rr', 'tt', 'hh', 'hhh', 'nn', 'ww']
ten_rows = rows[0:10]

for element in ten_rows:
    print(ten_rows[0:3])
    

#creating a list of lists
five_elements = ['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', \
                 '828'], ['Arlington', '503'], ['Atlanta', '1379']


cities_list = []

cities_list.append(five_elements[0][0])
cities_list.append(five_elements[1][0])
cities_list.append(five_elements[2][0])
cities_list.append(five_elements[3][0])
cities_list.append(five_elements[4][0])

print(cities_list)


five_elements = ['Albuquerque', '749'], ['Anaheim', '371'], ['Anchorage', \
                 '828'], ['Arlington', '503'], ['Atlanta', '1379']


cities_list = []

for row in five_elements:
    citynames = row[0]
    cities_list.append(citynames)
print(cities_list)


#Use the Boolean operators to determine if the following pairs
 #of values are equivalent:
#The first element in cities and the string "Albuquerque". 
#Assign the resulting Boolean
# value to first_alb.
#The second element in cities and the string "Albuquerque". Assign the
# resulting Boolean value to second_alb.
#The first element in cities and the last element in cities.
# Assign the resulting Boolean value to first_last.


# Boolean Operators

cities = ['Albuquerque', 'Anaheim', 'Anchorage', 'Arlington', 'Atlanta', 'Aurora', \
          'Austin', 'Bakersfield', 'Baltimore', 'Boston', 'Buffalo', \
          'Charlotte-Mecklenburg', 'Cincinnati', 'Cleveland', 'Colorado Springs',\
          'Corpus Christi', 'Dallas', 'Denver', 'Detroit', 'El Paso', \
          'Fort Wayne', 'Fort Worth', 'Fresno', 'Greensboro', 'Henderson', \
          'Houston', 'Indianapolis', 'Jacksonville', 'Jersey City', 'Kansas City',\
          'Las Vegas', 'Lexington', 'Lincoln', 'Long Beach', 'Los Angeles', \
          'Louisville Metro', 'Memphis', 'Mesa', 'Miami', 'Milwaukee', \
          'Minneapolis', 'Mobile', 'Nashville', 'New Orleans', 'New York', \
          'Newark', 'Oakland', 'Oklahoma City', 'Omaha', 'Philadelphia', \
          'Phoenix', 'Pittsburgh', 'Plano', 'Portland', 'Raleigh', 'Riverside', \
          'Sacramento', 'San Antonio', 'San Diego', 'San Francisco', 'San Jose', \
          'Santa Ana', 'Seattle', 'St. Louis', 'St. Paul', 'Stockton', 'Tampa', \
          'Toledo', 'Tucson', 'Tulsa', 'Virginia Beach', 'Washington', 'Wichita']

first_alb = cities[0] == "Albuquerque"
second_alb = cities[1] == "Albuquerque"
first_last = cities[0] == len(cities)-1

print(first_alb, second_alb, first_last, end='')


#Booleans with greater

#The variable crime_rates is a list of integers containing the crime
# rates from the dataset. Perform the following comparisons:
#Evaluate whether the first element in crime_rates is larger
# than the integer 500, and assign the Boolean result to first_500.
#Evaluate whether the first element in crime_rates is larger than
# or equal to 749, and assign the Boolean result to first_749.
#Evaluate whether the first element in crime_rates is greater 
#than or equal to the last element in crime_rates, and assign the 
#Boolean result to first_last.

crime_rates = [749, 371, 828, 503, 1379, 425, 408, 542, 1405, 835, 1288, 647, \
               974, 1383, 455, 658, 675, 615, 2122, 423, 362, 587, 543, 563, \
               168, 992, 1185, 617, 734, 1263, 784, 352, 397, 575, 481, 598, \
               1750, 399, 1172, 1294, 992, 522, 1216, 815, 639, 1154, 1993, \
               919, 594, 1160, 636, 752, 130, 517, 423, 443, 738, 503, 413, \
               704, 363, 401, 597, 1776, 722, 1548, 616, 1171, 724, 990, 169, \
               1177, 742]

first_500 = crime_rates[0] > 500
first_749 = crime_rates[0] >= 749
first_last = crime_rates[0] >= len(crime_rates)-1

print(first_500, first_749, first_last, end='')


#Booleans with less than

#The variable crime_rates is a list of integers containing the crime
# rates from the dataset. Perform the following comparisons:
#Evaluate whether the second element in crime_rates is smaller
# than the integer 500, and assign the Boolean result to second_500.
#Evaluate whether the second element in crime_rates is smaller than
# or equal to 371, and assign the Boolean result to second_371.
#Evaluate whether the second element in crime_rates is smaller 
#than or equal to the last element in crime_rates, and assign the 
#Boolean result to second_last.


second_500 = crime_rates[1] < 500
second_371 = crime_rates[1] <= 371
second_last = crime_rates[1] <= len(crime_rates)-1

print(second_500, second_371, second_last, end='')


# if statements

result = 0

myvar = (cities[2] == 'Anchorage')
if myvar:
        result += 1
        print(result)

value = 1500

if value > 500:
    if value > 1000:
        print("This number is HUGE!")


# Nesting if statements 

both_conditions = False

myvar = (crime_rates[0] > 500)
myvar1 = (crime_rates[1] > 300)

if myvar:
    if myvar1:
        both_conditions = True
print(myvar, myvar1)


# if statements and for loops

found = False
for city in cities:
    if city == 'Washington':
        found = True
        print(city)        


five_hundred_list = []

for cr in crime_rates:
    if cr > 500:
        five_hundred_list.append(cr)
        print(five_hundred_list)


# find the highest crime rate

print(crime_rates)

highest = (crime_rates[0])

for value in crime_rates:
    if (value > highest):
        highest = value
print(highest)        


#Read file into a string

k = open("dq_unisex_names.csv", "r")
names = k.read()

#converting the list to a list

names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

#converting a list of strings to a list of lists

nested_list = []

for element in names_list:
    comma_list = element.split(",")
    nested_list.append(comma_list)
    first_five = nested_list[0:5]
    print(first_five)

#convert numerical values

numerical_list = []

for element in nested_list:
    myvar = element[0]
    myvar1 = float(element[1])
    combine_vars = [myvar, myvar1]
    numerical_list.append(combine_vars)
    first_five = numerical_list[0:5]
    print(first_five)
    
 #Filtering list 

thousand_or_greater = []


for value in numerical_list:
    if value[1] >= 1000:
        thousand_or_greater.append(value[0])
        first_10_elements = thousand_or_greater[0:10]
        print(first_10_elements)



# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []


for value in numerical_list:
    greater_than_or_equals_a_thousand = value[1] >= 1000
    if greater_than_or_equals_a_thousand:
        thousand_or_greater.append(value[0])
        first_10_elements = thousand_or_greater[0:10]
        print(first_10_elements)
    


# working with la_weather.csv

#Create an empty list and assign to weather_data.
#Open and read in la_weather.csv.
#Split the data on the newline character to convert it to a list of rows.
#Split each row on the comma and append each list to weather_data.

weather_data = []
v = open("la_weather.csv", "r")
la_weather = v.read()
la_data = la_weather.split("\n")

for data in la_data:
    comma_split = data.split(",")
    weather_data.append(comma_split)

#getting a single column from the data

# weather_data has already been read in automatically to make
# things easier.
weather = []

for row in weather_data:
    element2 = row[1]
    weather.append(element2)
 
# removing the header

#Slice the weather list to remove the header.
#The slice should only remove the first element in the list.
#Assign the slice to new_weather.

new_weather = []
new_weather = weather[1::]

#we can also use this
new_weather = []
last_element = len(weather)
new_weather = weather[1:last_element]

# the in statement

#Use the in statement to check whether the value cat is in the
#list animals, and assign the result to cat_found.
#Use the in statement to check whether the value space_monster 
#is in the list animals, and assign the result to space_monster_found.

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals
space_monster_found = "space_monster" in animals

print(space_monster_found, cat_found )


new_weather = ['Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny',
 'Sunny','Fog','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny',
 'Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Fog-Rain','Rain',
 'Fog-Rain','Rain','Sunny','Sunny','Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Fog',
 'Fog',
 'Sunny',
 'Rain',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Rain',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Rain',
 'Rain',
 'Rain',
 'Sunny',
 'Thunderstorm',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog-Rain',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Rain',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog-Rain',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Rain',
 'Rain',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog']
#
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", \
                 "Type of Weather"]
weather_type_found = []

for item in weather_types:
    item_occur = item in new_weather
    weather_type_found.append(item_occur)
print(weather_type_found)

#Assign the first element of weather to first_element and display it using
# the print() function.
#Assign the last element of weather to last_element and display it using
# the print() function.
    
# Weather has been loaded in.

weather = ['Type of Weather', 'Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Sunny',
 'Sunny','Fog','Rain','Sunny','Sunny','Sunny','Sunny','Sunny','Fog','Sunny',
 'Sunny','Sunny','Sunny','Sunny','Sunny','Rain','Fog-Rain','Rain',
 'Fog-Rain','Rain','Sunny','Sunny','Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Fog',
 'Fog',
 'Sunny',
 'Rain',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Rain',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Rain',
 'Rain',
 'Rain',
 'Sunny',
 'Thunderstorm',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog-Rain',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Rain',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog-Rain',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Rain',
 'Rain',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Rain',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Sunny',
 'Fog',
 'Fog',
 'Fog']

first_element = weather[0]
print(first_element)

last_element = str(len(weather))
print(last_element)



#Dictionaries

#practising populating a dictionary
#Assign the value 1 to the key Aquaman in a new dictionary
# named superhero_ranks.
#Assign the value 2 to the key Superman in superhero_ranks

superhero_ranks = {} # define dictionary

superhero_ranks["Aquaman"] = 1  #assign key and values
superhero_ranks["Superman"] = 2


#Look up FDR in president_ranks and assign the result to a new 
#variable fdr_rank.
#Look up Lincoln in president_ranks and assign the result to a 
#new variable lincoln_rank.
#Look up Aquaman in president_ranks and assign the result to a 
#new variable aquaman_rank.

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3

fdr_rank = president_ranks["FDR"]
lincoln_rank = president_ranks["Lincoln"]
aquaman_rank = president_ranks["Aquaman"]

print(fdr_rank, lincoln_rank, aquaman_rank)
#
#defining a dictionary with values
#
#Create a dictionary named animals with the following keys and values:
#The key 7 corresponding to the value raven.
#The key 8 corresponding to the value goose.
#The key 9 corresponding to the value duck.
#Create a dictionary named times with the following keys and values:
#The key morning corresponding to the value 9.
#The key afternoon corresponding to the value 14.
#The key evening corresponding to the value 19.
#The key night corresponding to the value 23.

random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", \
                 3: 5.6}
print(random_values)

animals = {7:"raven", 8:'goose', 9:'duck'}
times = {"morning":9, 'afternoon':14, 'evening':19, 
        'night':23}

#modifying dictionary values

students = {
    "Tom": 60,
    "Jim": 70
}

students ["Ann"] = 85 #Add the key Ann and value 85 to the dictionary students.
students ["Tom"] = 80 #Replace the value for the key Tom with 80.
students ["Jim"] = students ["Jim"] + 5 #Add 5 to the value for the key Jim.


#the in statement and dictionaries

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}

#Check whether jupiter is a key in planet_numbers, 
#and assign the resulting 
#Boolean value to jupiter_found.
#jupiter_found = "jupiter" in planet_numbers

#Check whether earth is a key in planet_numbers, and assign the 
#resulting Boolean value to earth_found.
#earth_found = "earth" in planet_numbers
#
#print(jupiter_found, earth_found)


#practising with the else statement

#Append any names in planet_names that are longer than 5 characters to 
#long_names. Otherwise, append the names to short_names. To accomplish this:
#Loop through each item in planet_names.
#Use the len() function to find the length of the item.
#If the length is greater than 5, append the item to long_names.
#Otherwise, append it to short_names.
#When complete, short_names should contain any planet names less than 
#6 characters long, and long_names should contain any planet names 6 
#characters or longer.

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", \
                "Neptune", "Uranus"]
short_names = []
long_names = []

for item in planet_names:
    len(item)
    if len(item) > 5:
        long_names.append(item)
    else:
        short_names.append(item)    
print(long_names, short_names)


#counting with dictionaries

#Count the number of times that each element occurs in the 
#list named pantry that appears in the code block below. You'll need to:

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", \
          "tomato", "potato", "grape"]

##Create an empty dictionary named pantry_counts.
#
pantry_counts = {}

##Loop through each item in pantry.
for item in pantry:
    #If the item appears in pantry_counts, add 1 to the value in 
    #pantry_counts for the item's key.
    if item in pantry_counts: 
        pantry_counts[item] = pantry_counts[item] + 1
    #Otherwise, add the item to pantry_counts as a key, with the value 1.
    else:
        pantry_counts[item] = 1 
print(pantry_counts)


#counting the weather
#Count how many times each type of weather occurs in the weather list, 
#and store the results in a new dictionary called weather_counts.

weather_counts = {}

for item in new_weather:
    if item in weather_counts:
        weather_counts[item] = weather_counts[item] + 1
    else:
        weather_counts[item] = 1
print(weather_counts)

sunny_value = weather_counts ["Sunny"]
print(sunny_value)


#introduction to functions
#Read movie_metadata.csv into a list of lists and assign to movie_data.

# Open and read the file movie_metadata.csv into a string variable.
R = open("movie_metadata.csv", 'r')
Data = R.read()

#Split the data into rows on the newline character ("\n").
idb_mini = Data.split("\n")
#Create an empty list, movie_data.
movie_data = []

#Loop through each row, and split each row into a list on 
#the comma character (","), and append it to movie_data.
for row in idb_mini:
    comma_list = row.split(",")
    movie_data.append(comma_list)

#Display the first 5 lists in movie_data using the print() function.
    first_five_list = movie_data[0:5]
#    
    print(first_five_list )


    
#Write a function, with a definition, name, argument(s), 
#body and return value, that returns a list containing the names 
#of the movies in movie_data. This function is expected to behave 
#similar to first_elt(), but for multiple lists.

#Give the function a name that describes what it does; 
#first_elts() is a good example, but feel free to be creative.
def first_names(input_0):
    
#Declare an empty list.    
    empty_list = []
    
#Use a for loop to extract the first element of each list, 
#and append these elements to the empty list.    
    for element in movie_data:
        names = element[0]
        empty_list.append(names)
        
#Return the list.        
    return empty_list

#Assign the returned list to movie_names.
movie_names = first_names(movie_data)

#Display the first 5 elements of movie_names using the print() function.
first_five = movie_names[0:5]
print(first_five)


#functions with multiple return paths
wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot',\
                'English','USA',2017]

#Write a function named is_usa() that checks whether or not a movie
# was made in the United States.
def is_usa(input):
    for item in input:
        if item == "USA":
            return True
    else:
        return False
        
wonder_woman_usa = is_usa(wonder_woman)
print(wonder_woman_usa)


#function with multiple arguments
def equals_str(input_lst,input_str):
    if input_lst[6] == input_str:
        return True
    else:
        return False
wonder_woman_random = equals_str(wonder_woman,"UK")
print(wonder_woman_random)

def index_equals_str(input_lst, index, input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
    
    
wonder_woman_in_color = index_equals_str(wonder_woman, 2, 'Color')
print(wonder_woman_in_color)


#function with optional argument
def feature_counter(input_1st, index, input_str, header_row = False):
    counter = 0
    if header_row == True:
        input_1st[1:len(input_1st)]
    for element in input_1st:
        if input_1st[index] == input_str:
            counter += 1
            return counter
        
num_of_us_movies = feature_counter(wonder_woman, 6, "USA")
print(num_of_us_movies)


#Calling a function inside another function

#Write a summary_statistics() function that will take movie_data 
#as input, and output a dictionary that will give useful numbers from the data.

#Define summary_statistics() with one argument, an input list.

def summary_statistics(input_1st):
#Use the feature_counter() with the relevant arguments to count the 
#following properties and make them equal to the corresponding variables.

#Assign the number of movies made in Japan to num_japan_films.
    num_japan_films = feature_counter(wonder_woman, 6, "Japan", True)
#Assign the number of movies made in usa to num_usa_films.
    num_usa_films = feature_counter(wonder_woman, 6, "USA", True)
#Assign the number of movies in color to num_color_films.
    num_color_films = feature_counter(wonder_woman, 2, "Color", True)
#Assign the number of movies in English to num_films_in_english.
    num_films_in_english = feature_counter(wonder_woman, 5, "English", True)
#Create a dictionary that associates the keys (japan_films,color_films,
#films_in_english) with the corresponding variables.    
    films_category = {"japan_films":num_japan_films, "color_films":\
                     num_color_films, "films_in_english":\
                     num_films_in_english, "usa_films":num_usa_films}
#Return the dictionary.
    return films_category
#Call the function with movie_data as its input, and store its value in
# summary.
summary = summary_statistics(wonder_woman)
print(summary)
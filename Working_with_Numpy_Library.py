# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:29:21 2017

@author: bEgbedokun
"""
### Working with Modules in Python
import csv
m = open("nfl.csv")
nf = csv.reader(m)
nfl = list(nf)

#In the following cell, add code that:
#Imports and uses the csv module to load data from our "nfl.csv" file.
#Counts how many games the "New England Patriots" won from 2009-2013 .
#To do this, set a counter to 0 and increment by 1 for each row that
# has "New England Patriots" in the winner column.
#Assigns the count to patriots_wins.

#import csv
m = open("nfl.csv")
nf = csv.reader(m)
nfl = list(nf)

patriots_wins = 0

for row in nfl:
    if row[2] == "New England Patriots":
        patriots_wins += 1
        
#Write a function called nfl_wins that takes a team name as input.
#The function should return the number of games the team won in the period 
#covered by the data set.
#Use the function to assign the number of "Dallas Cowboys" wins to cowboys_wins.
#Use the function to assign the number of "Atlanta Falcons" wins to falcons_wins.


#import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

## Define your function here.

def nfl_wins(club_name):
    team_wins = 0
    for row in nfl:
        if row[2] == club_name:
            team_wins += 1
    return team_wins

cowboys_wins = nfl_wins("Dallas Cowboys")

falcons_wins = nfl_wins("Atlanta Falcons")


#Introduction to Classes and Objects
#Defining the Dataset class

class Dataset:
    def __init__(self):
        self.type = "csv"
        
dataset = Dataset()
print(dataset.type)

#passing additional argument to the initializer
#import csv
class Dataset:
    def __init__(self, data):
        self.data = data

f = open("nfl.csv", 'r')
csvreader = csv.reader(f)
nfl_data = list(csvreader)

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

#Adding additional behaviour
class Dataset:
    def __init__(self, data):
        self.data = data
        
    # Your method goes here
    def print_data(self):
        # New method **remember to add self**.
        print(self.data[:5])
#create instance        
nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data()


# Enhancing the initializer
# Default display code
class Dataset:
    def __init__(self, data):
        self.data = data
        self.header = self.data[0]
        self.data = self.data[1:]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

#Grabbing column data

# Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, value in enumerate(self.header):
            if label == value:
                index = idx

        column = [] 
        for row in self.data: 
            column.append(row[index])
        return column
            
                
    
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')
#
#
##Count unique method
#
## Default display code
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def count_unique(self, label):
        full_column = self.column(label)
        total_count = len(set(full_column))
        return total_count
    
    # Add your count unique method here

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')


#Make Object Human Readable

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def count_unique(self, label):
        full_column = self.column(label)
        total_count = len(set(full_column))
        return total_count
    
    def __str__(self, data):
        return str(self.data[:10])

nfl_dataset = Dataset(nfl_data)
print(nfl_dataset.__str__(nfl_dataset))


#creating Arrays

import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

##Array shape
vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])


vector_shape = vector.shape
matrix_shape = matrix.shape
#
print(vector_shape, matrix_shape)
#
#
##Using Numpy
import numpy as np
world_alcohol =  np.genfromtxt("C:/Users/bEgbedokun/Documents/World_alcohol.txt"\
                                  , dtype = "U75", skip_header = 1, delimiter = ",")
print(type(world_alcohol))
#
##Data types
#import numpy
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)


#Indexing arrays

#Assign the amount of alcohol Uruguayans drank in other beverages per capita
# in 1986 to uruguay_other_1986. This is the second row and fifth column.
uruguay_other_1986 = world_alcohol[1, 4]

#Assign the country in the third row to third_country. Country is the third
# column.
third_country = world_alcohol[2, 2]

#Slicing arrays

#Assign the whole third column from world_alcohol to the variable countries
countries = world_alcohol[:, 2]

#Assign the whole fifth column from world_alcohol to the variable 
#alcohol_consumption
alcohol_consumption = world_alcohol[:, 4]


#Slicing one dimension
matrix = np.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])

print(matrix[:,0:2])
print(matrix[1:3,:])
print(matrix[1:3,1])


#Slicing one dimension

#Assign all the rows and the first 2 columns of world_alcohol to first_two_columns
first_two_columns = world_alcohol[:, 0:2]

#Assign the first 10 rows and the first column of world_alcohol to first_ten_years
first_ten_years = world_alcohol[0:10, 0]

#Assign the first 10 rows and all of the columns of world_alcohol to first_ten_rows
first_ten_rows = world_alcohol[0:10, :]

#Slicing two dimension

matrix = np.array([
                    [5, 10, 15], 
                    [20, 25, 30],
                    [35, 40, 45]
                 ])
print(matrix[1:3,0:2])

#Assign the first 5 rows of the columns at index 1 and 2 of world_alcohol
# to first_five_regions
first_five_regions = world_alcohol[:5, 1:3]
print(first_five_regions)


#Array comparisons

#Extract the third column in world_alcohol, and compare it to the string 
#Canada. Assign the result to countries_canada
countries_canada = world_alcohol[:, 2] == "Canada"

#Extract the first column in world_alcohol, and compare it to the string 1984. 
#Assign the result to years_1984
years_1984 = world_alcohol[:, 0] == "1984"


#Selecting Elements

#Compare the third column of world_alcohol to the string Algeria.
#Assign the result to country_is_algeria.
country_is_algeria = (world_alcohol[:, 2] == "Algeria")

#Select only the rows in world_alcohol where country_is_algeria is True.
#Assign the result to country_algeria
country_algeria = world_alcohol[country_is_algeria]


#Comparisons with multiple conditions

#Perform a comparison with multiple conditions, and join the conditions 
#with &.Compare the first column of world_alcohol to the string 1986.
#Compare the third column of world_alcohol to the string Algeria.
#Enclose each condition in parentheses, and join the conditions with &.
#Assign the result to is_algeria_and_1986.
is_algeria_and_1986 = (world_alcohol[:, 0] == "1986") & (world_alcohol[:, 2]\
                      == "Algeria")

#Use is_algeria_and_1986 to select rows from world_alcohol.
#Assign the rows that is_algeria_and_1986 selects to rows_with_algeria_and_1986
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986]


#Replacing values

#Replace all instances of the string 1986 in the first column of world_alcohol
# with the string 2014
is_string_1986 = world_alcohol[:, 0] == "1986"
world_alcohol[is_string_1986, 0] = "2014"

#Replace all instances of the string Wine in the fourth column of world_alcohol
# with the string Grog
is_string_wine = world_alcohol[:, 3] == "Wine"
world_alcohol[is_string_wine, 3] = "Grog"

#Replacing the empty strings

#Compare all the items in the fifth column of world_alcohol with an empty 
#string ''. Assign the result to is_value_empty
is_value_empty = world_alcohol[:, 4] == ''

#Select all the values in the fifth column of world_alcohol where 
#is_value_empty is True, and replace them with the string 0
world_alcohol[is_value_empty, 4] = '0'


#Converting data types

#Extract the fifth column from world_alcohol, and assign it to the 
#variable alcohol_consumption, remember to resovle empty items
alcohol_consumption = world_alcohol[:, 4] == ''

#replace all 'nulls' by '0'
world_alcohol[alcohol_consumption, 4] = '0'

#Use the astype() method to convert alcohol_consumption to the float data type.
alcohol_consumption = alcohol_consumption.astype(float)


#Computing with Numpy

#Use the sum() method to calculate the sum of the values in alcohol_consumption. 
#Assign the result to total_alcohol
total_alcohol = alcohol_consumption.sum()
print(total_alcohol)
#Use the mean() method to calculate the average of the values in alcohol_consumption.
# Assign the result to average_alcohol
average_alcohol = alcohol_consumption.mean()


#Total Annual Alcohol Consumption

#Create a matrix called canada_1986 that only contains the rows in world_alcohol
# where the first column is the string 1986 and the third column is the string 
#Canada
is_canada_1986 = (world_alcohol[:, 0] == "1986") & (world_alcohol[:, 2] == "Canada")
canada_1986 = world_alcohol[is_canada_1986, :]

#Extract the fifth column of canada_1986, replace any empty strings ('') 
#with the string 0, and convert the column to the float data type.
# Assign the result to canada_alcohol
canada_alcohol = canada_1986[:, 4]

empty_strings = canada_alcohol == ''
canada_alcohol[empty_strings] = '0'
canada_alcohol = canada_alcohol.astype(float)

#Compute the sum of canada_alcohol. Assign the result to total_canadian_drinking
total_canadian_drinking = canada_alcohol.sum()


#Calculating Consumption for each Country
#totals should contain all of the country names as keys, with the corresponding alcohol consumption totals for 1989 as values
totals = {}
is_year_1989 = (world_alcohol[:, 0] == '1986') 
year = (world_alcohol[is_year_1989, :])



for country in countries:
    country_ = year[:, 2] == country
    country_consumption = year[country_, :]
    alcohol_quantity = country_consumption[:, 4]
    empty_row = alcohol_quantity == ''
    alcohol_quantity[empty_row] = '0'
    
    alcohol_quantity = alcohol_quantity.astype(float)
    totals[country] = alcohol_quantity.sum()
    
print(totals)


#Finding the Country that Drinks the most

highest_value = 0
highest_key = None

for key in totals:
    num = totals[key]
    if highest_value < num:
        highest_value = num
        highest_key = key

    
    
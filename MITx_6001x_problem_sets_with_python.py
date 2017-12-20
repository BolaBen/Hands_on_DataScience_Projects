# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:30:14 2017

@author: bEgbedokun
"""
#Problem 1
#Assume s is a string of lower case characters.
#
#Write a program that counts up the number of vowels 
#contained in the string s. 
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
# if s = 'azcbobobegghakl', your program should print:
#
#Number of vowels: 5

s = 'what i wish to become'
count = 0

  
for letter in s:
    if letter == 'a' or letter == 'e' or letter == 'i' \
        or letter == 'o' or letter == 'u':
            count += 1
print("Number of vowels: ", count)



#Problem 2            
#Assume s is a string of lower case characters.
#
#Write a program that prints the number of times
# the string 'bob' occurs in s. For example, 
# if s = 'azcbobobegghakl', then your program should print
#
#Number of times bob occurs is: 2

s ='boobobobobobbobobbobwboboboolaobzrbo'
count = 0

for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1
print('Number of times bob occurs is: ', (count))
    
    
#Problem 3

#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring
# of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', 
# then your program should print
#
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. 
#For example, if s = 'abcbcd', then your program should print
#
#Longest substring in alphabetical order is: abc


s = 'dtlashxx'

maxSub, currentSub, previousChar = '', '', '' # define variables
for char in s: # a for loop to index s
    if char >= previousChar:     # test case 1
        currentSub = currentSub + char    # values to save
        if len(currentSub) > len(maxSub):  # test case 2
            maxSub = currentSub       # values to save
    else: currentSub = char
    previousChar = char
print("Longest substring in alphabetical order is:", maxSub)



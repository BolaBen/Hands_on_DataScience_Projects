# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:55:28 2017

@author: bEgbedokun
"""
#ESTIMATED TIME TO COMPLETE: 5 minutes
#In this problem you'll be given a chance to practice writing some while loops.
#
#1. Convert the following into code that uses a while loop.
#
#print 2
#prints 4
#prints 6
#prints 8
#prints 10
#prints Goodbye!


num = 2
while num < 12:
    print(num)
    num += 2
    if num > 10:
        print('Goodbye')




#ESTIMATED TIME TO COMPLETE: 5 minutes
#
#2. Convert the following into code that uses a while loop.
#
#prints Hello!
#prints 10
#prints 8
#prints 6
#prints 4
#prints 2

print("Hello!")
numb = 12


while numb != 0:
    numb -= 2
    print(numb)
    if numb == 2:
        break

#ESTIMATED TIME TO COMPLETE: 5 minutes
#
#3. Write a while loop that sums the values 1 through end, inclusive. end is a 
#variable that we define for you. So, for example, if we define end to be 6, your 
#code should print out the result:
#
#21
#which is 1 + 2 + 3 + 4 + 5 + 6.
#
#For problems such as these, do not include input statements or define 
#variables we will provide for you. Our automating testing will provide values
# so write your code in the following box assuming these variables are already defined.
#
#Hint: Don't Use A Variable Called 'sum'

end = 6
i = 0
total_added_element = 0

while i < end:
    i += 1
    total_added_element += i
    if i == end:
        print(total_added_element)
    
          

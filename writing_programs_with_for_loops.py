# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:29:47 2017

@author: bEgbedokun
"""
#ESTIMATED TIME TO COMPLETE: 5 minutes
#In this problem you'll be given a chance to practice writing some while loops.
#
#1. Convert the following into code that uses a for loop.

##print 2
##prints 4
##prints 6
##prints 8
##prints 10
##prints Goodbye!


for i in range(2,11,2):
    print(i)
    if i == 10:
        print('Goodbye!')
        


        
#ESTIMATED TIME TO COMPLETE: 5 minutes
#
#2. Convert the following into code that uses a while loop.

##prints Hello!
##prints 10
##prints 8
##prints 6
##prints 4
##prints 2

print('Hello!')
for i in range(10,0,-2):
    print(i)



#ESTIMATED TIME TO COMPLETE: 5 minutes
#
#3. Write a for loop that sums the values 1 through end, inclusive. end is a 
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

end = 7
myadded_element = 0
i = 0

for i in range(1, end+1):
    myadded_element += i
    if i == end:
        print(myadded_element)
    

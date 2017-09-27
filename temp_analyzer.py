# -*- coding: utf-8 -*-
"""
Converting degrees Fahrenheit into degrees Clesius and assigning them into corresponding temperature classes.

This script imports the necessary modules and creates an empty list. After which the list tempData imported,
containing temperature values in Fahrenheit, will be iterated over during which functions from module functions
are implemented.

First, in the for loop the input Fahrenheit values from the list will be converted into degree Celsius by using
the fahrToCelsius() function. Secondly, they will be assigned to temperature classes specified in the tempClassifier()
function. After these steps have been performed, the classes will be added to the tempClasses list.

Finally, the amount of each class in the tempClasses list is counted with the .count() function and the results
are printed out.

Author: 
    Mira Kajo - 27.9.2017
"""
# Import the necessary modudes into Python:
import data
# Import functions module in a shorter version in order to type less when applying it in the code:
import functions as f

# Create an empty list:
tempClasses = []

# Iterate over the Fahrenheit temperatures in tempData list:
    # Adding the module name in front of the list:
for temp in data.tempData:
    # Converting the Fahrenheit values into Celsius with fahrToCelsius() function:
        # Also, adding the module abbreviation in front of the function:
    tempCelsius = f.fahrToCelsius(temp)
    
    # Assigning the newly minted Celsius temperatures into corresponding temperature classes:
    tempClass = f.tempClassifier(tempCelsius) 
    
    # Adding the values to the empty list:
    tempClasses.append(tempClass)
    

    
# Using the .count() function to fetch the amount of specific numbers (classes) within the tempClasses- list:    
count_zero = tempClasses.count(0)
count_one = tempClasses.count(1)
count_two = tempClasses.count(2)
count_three = tempClasses.count(3)

# Printing out the count of each class:
print("Class zero has:", count_zero, " entries.")
print("Class one has:", count_one, " entries.")
print("Class two has:", count_two, " entries.")
print("Class three has:", count_three, " entries.")
# -*- coding: utf-8 -*-
"""
Contains two functions:
    Function to be used when converting degrees Fahrenheit into degrees Celsius --> fahrToCelsius.
    
    Function to be used when classifying degrees Celsius into specific classes --> tempClassifier.

Author: 
    Mira Kajo - 27.9.2017
"""

# Define a function which converts the Fahreinheit temperature given as input
# to degrees Celsius:
def fahrToCelsius(tempFahrenheit):
    ''' This function returns the input Fahrenheit value in corresponding degrees Celsius.
    
    Parameters
    ----------
    tempFahrenheit: <numerical>
        Temperature in degrees Fahrenheit
        
    Returns
    -------
    <float>
        Temperature in degrees Celsius
    '''
    # assign the result of the conversion into a new variable convertedTemp:
        # note to self: remember to add parenthesis as it dictates the order of the calculations!
    convertedTemp = (tempFahrenheit - 32) / 1.8
    
    # return the value of convertedTemp once the function is implemented and printed:
    return convertedTemp
    

# Define a function which classifies the class into which the input temperature falls according to given
# conditions. The function shall return the class number as output:
def tempClassifier(tempCelsius):
    ''' This function return the temperature class of an input temperature.
    
    Parameters
    ----------
    tempCelsius: <numerical>
        Temperature in degrees Celsius
        
    Returns
    -------
    <integer>
        Returns the number of the temperature class
    '''
    
    # Define a conditional statement which analyses the input temperature value, and returns the correct class number:
    if tempCelsius < -2:
        return 0
    elif tempCelsius <= 2:
        return 1
    elif tempCelsius <= 15:
        return 2
    elif tempCelsius > 15:
        return 3
    # Optionally:
    #else:
        #return 3

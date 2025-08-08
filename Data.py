# Program focus, relates to real-life data, Caffenie level in drinks.
# Program is organized, uses reasonable variable names, code runs without errors.

# Importing csv so I can link my excel file with my code.
import csv

# The file gets linked.

filename = open('CaffeineContentOfDrinks.csv', 'r')

# Reads the file.
# Streach Points: Learning how to use Dictonary.
dataReader = csv.DictReader(filename)

# Creating a Dictonary List.
dataRows = []

# Add rows from the excel file in the Dictonary List. Used a for loop.
for row in dataReader:
    dataRows.append(row)

# Created the first list, Added the correct columns in the list. Used a for loop.
drinks = []
for column in dataRows:
    drinks.append(column['Drink'])

# Created the second list, Added the corrrect columns in the list. Used a for loop.
caffeine = []
for column in dataRows:
    caffeine.append(int(column['Caffeine']))

# Created the third list, Added the correct columns in the list. Used a for loop.
calories = []
for column in dataRows:
    calories.append(int(column['Calories']))

# Creates the user input. Has 2 results.

# Creating the question.

# The user is asked for a number range, the dictonary will read the file and put it into a list, and find the list that matches the values the user has inputed.
high = input("Enter high caffeine value: ")
low = input("Enter low caffeine value: ")


# Using dictonary to find the drink with the highest level of caffeine, answering my question.

# Made variables.
index = 0
counter = 0
caffeineLvl = 0

# Made a dictonary list.
caffeineDict = {}
found = 0
# Made a for loop with an if statement inside of it. Converted the characters into integers.
for column in dataRows:
    if (int(column['Caffeine']) >= int(low) and int(column['Caffeine']) <= int(high)):
        index = counter
        print("Drink: ",drinks[index],"\tCaffeine: ",caffeine[index], "\tCalories: ", calories[index])
        found = 1
    counter = counter + 1
    
if found == 0:
    print("Range does not exist.")

#-----------------------------------------------------------------------------
# Name:        Lab-02 (Lab 02.py)
# Purpose:     Apply apprehended concepts and knowledge of conditional statements through hands-on learning
#
# Author:      Brian Z.
# Created:     02-Mar-2026
# Updated:     02-Mar-2026
#-----------------------------------------------------------------------------

# Allow for program to explicitly receive an integer value input
grade = int(input("What is your grade? "))

# Check if the entered value that is assigned to the grade variable is, according to certain set standards, 80 or above while also seeing if the score is valid as to make sure that the following "else if" statements are considered in the case that the provided integer is unrealistically above 100
if 80 <= grade <= 100:
  print("Exceeding Expectations.")
  
# Examine if the given number is within a specific range which is deemed to be, quote unquote, "meeting expectations"
elif 70 <= grade <= 79:
  print("Meeting Expectations.")

# Look over the singular variable and evaluate if said item lies between a range designated to the message: "Needs Improvement."
elif 50 <= grade <= 69:
  print("Needs Improvement.")

# Gauge the possibility of the inputted numerical amount being invalid and act upon accordingly should the chance happen
elif grade < 0 or 100 < grade: 
  print("Invalid Grade.")

# Encountering the situation that the stated score does not meet any of the previous condition(al)s, render the program to output a message that communicates the achievement of subpar grade
else:
  print("Not Passing.")
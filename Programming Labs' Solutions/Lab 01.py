#-----------------------------------------------------------------------------
# Name:        Lab-01 (Lab 01.py)
# Purpose:     Internalize rudimentary yet necessary concepts of storing values of different "primitive" data types, type casting, output formatting and receiving input through minds-on execution
#
# Author:      Brian Z.
# Created:     27-Feb-2026
# Updated:     01-Mar-2026
#-----------------------------------------------------------------------------

# Take in stream of input information on machine/users' attributes
name_replied = input("What is your name? ")
years_of_age = input("\nHow old are you? ")
print(f"\nHello {name_replied}, you are currently {years_of_age} years old.")

# Reinitialize variable that has been tasked with storing an interpretable form of numerical quantity which, in this case, is how many years old an entity is said to be with ten added on to it; follow this by outputing the amount in a clarified context of the English language as opposed to in and of itself using Python
years_of_age = int(years_of_age) + 10
print(f"In 10 years, you will be {years_of_age} years old.")

# Seek out and fetch numbers from the continued feed-in of input
intially_entered_number = int(input("Enter a number: "))
next_set_number = int(input("\nEnter another number: "))

# Repeatedly print out terms that depict mathematical operations and the corresponding results that are yielded when applying said calculations on the obtained integers from prior
print(f"\nSum: {intially_entered_number + next_set_number}")
print(f"Difference: {intially_entered_number - next_set_number}")
print(f"Product: {intially_entered_number * next_set_number}")
print(f"Quotient: {intially_entered_number / next_set_number}")
print(f"Integer Division: {intially_entered_number // next_set_number}")
print(f"Modulo: {intially_entered_number % next_set_number}")
print(f"Power: {intially_entered_number ** next_set_number}")
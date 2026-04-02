#-----------------------------------------------------------------------------
# Name:        Lab-04 (Lab 04.py)
# Purpose:     Experiment with strings and functions/methods/references to interact and or potentially mutate them
#
# Author:      Brian Z.
# Created:     11-Mar-2026
# Updated:     11-Mar-2026
#-----------------------------------------------------------------------------

# Make the code prompt input to the user/machine and display an appropiate preceding message to give context
password = input("Enter password: ")

# Declare variables to keep track of the attributes that make the inputted passcode valid as a one-pass over the string cannot juggle each of the checks for stipulations without storing them at all
has_min_chars = False
has_uppercase = False
has_lowercase = False
digit_counter = 0

# Issue the first check for password length to be at least of eight characters; store the verdict in a designated variable for later use and other mutually exclusive checks
if 8 <= len(password):
  has_min_chars = True

# Iterate over the entirety of the string and check the relevant attributes of the letter at each interval and "stop"
for letter in range(0, len(password), 1):
  if password[letter].isupper():
    has_uppercase = True
  elif password[letter].islower():
    has_lowercase = True 
  elif password[letter].isdigit():
    digit_counter += 1

# We check if all above conditions are met and, if so, output a corresponding and notifying message to the user/machine
if has_min_chars and has_uppercase and has_lowercase and digit_counter == 1:
  print("Password is valid.")

# Tie the given error messages to the case(s) where the requirements for password being valid are not met; something else that is noteworthy is that these outputs are executed in a specific order as well
if not has_min_chars:
  print("Error: Password must be at least 8 characters long.")

if not has_lowercase:
  print("Error: Password must contain at least one lowercase letter.")

if not has_uppercase:
  print("Error: Password must contain at least one uppercase letter.")

if digit_counter != 1:
  print("Error: Password must contain exactly one digit.")
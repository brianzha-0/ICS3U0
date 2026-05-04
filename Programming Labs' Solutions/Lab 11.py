#-----------------------------------------------------------------------------
# Name:        Lab-11 (Lab 11.py)
# Purpose:     Apply learned concepts of exception/error handling including but not limited to: try/except and printing corresponding messages accordingly
#
# Author:      Brian Z.
# Created:     01-May-2026
# Updated:     04-May-2026
#-----------------------------------------------------------------------------



item_costs = {"apples": 2.50, "bananas": 1.75, "milk": 3.00}
item_list = ["apples", "bananas", "milk"]

#1: KeyError
item_name = input("Which item price do you want to check? ")

try: 
  print(f"The price of {item_name} is ${item_costs[item_name]}")
except:
  print(f"Sorry, {item_name} is not on the price list.")


#2: TypeError
budget = 10.00

try:
  num_people = input("How many people are sharing the cost? ")
  cost_per_person = budget / int(num_people)
  print(f"That will be ${cost_per_person:.2f} per person.")
except:
  print("Invalid Number")

  
#3: IndexError
print("Checking the 6th item on your list...")

try:
  item = item_list[5]
  print(f"The 6th item is {item}.")
except:
  print("There is no 6th item")


#4: TypeError
try:
  message = "You have " + len(item_list) + " items on your list."
  print(message)
except:
  print("You have " + str(len(item_list)) + " items on your list.")


#5: NameError
try:
  print(final_greeting)
except:
  print("Goodbye!")
#-----------------------------------------------------------------------------
# Name:        Key, Valued Exercises (key_valued_exercises.py)
# Purpose:     Allow people who enjoy and/or engage in exercising to edit set times
#
# Author:      Brian Z.
# Created:     20-May-2026
# Updated:     20-May-2026
#-----------------------------------------------------------------------------

# provide a list here of where you've used your additional module
# as well as the source of where you learned about it

import tkinter as tk
import math

def change_duration(dct, exercise, time):
  dct[exercise] = time
  return dct



def convert_to_seconds(minutes: int):
  return minutes * 60

dct = {"Lunges": 0.00, "Jumping": 0.00, "Jogging in Place": 0.00, "Salsa Steps": 0.00, "Jumping Jacks": 0.00, "Planks": 0.00}

try:
  upd = float(input("How long would you like to perform this set for: "))
except TypeError:
  raise TypeError("Please enter a valid numeric value, preferably one with decimal points")
  upd = float(input("How long would you like to perform this set for: "))

for key in dct:
  print(f"Key: {key}, Value: {dct[key]}")
  
  try:
    upd = float(input("How long would you like to perform this set for: "))
  except TypeError:
    raise TypeError("Please enter a valid numeric value, preferably one with decimal points")

  if 0 < upd:
    change_duration(dct, key, upd)
  else:
    del dct[key]

for itm in dct:
    print(f"You performed a set of {itm} for {convert_to_seconds(dct[itm])} seconds! Congrats!!")
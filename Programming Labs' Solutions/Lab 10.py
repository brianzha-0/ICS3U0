#-----------------------------------------------------------------------------
# Name:        Lab-10 (Lab 10.py)
# Purpose:     As a step up from the lists' data structure used throughout different algorithmic processes, dictionaries in Python allow for extensive capabilities in possibly more (yet still specific) use cases portrayed best through practical means
#
# Author:      Brian Z.
# Created:     27-Apr-2026
# Updated:     27-Apr-2026
#-----------------------------------------------------------------------------

dct = {}

while True:
  itm = input("Item: ")

  if itm == "done":
    break
  
  qtn = int(input("Quantity: "))

  if not itm in dct:
    dct[itm] = qtn
    
  else:
    dct[itm] = int(dct[itm]) + qtn

for itm in dct:
  print(f"{itm}: {dct[itm]}")
  
if not "apples" in dct:
  print("Are you sure you don't want apples?")

elif 10 < int(dct["apples"]):
  print("That's too many apples!")

if "oranges" in dct:
  if 5 < int(dct["oranges"]):
    dct["oranges"] = int(dct["oranges"]) - 5
    
  elif int(dct["oranges"]) <= 5:
    del dct["oranges"]

for itm in dct:
  print(f"{itm}: {dct[itm]}")
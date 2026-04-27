#-----------------------------------------------------------------------------
# Name:        Lab-09 (Lab 09.py)
# Purpose:     Practice using lists programmatically
#
# Author:      Brian Z.
# Created:     24-Apr-2026
# Updated:     27-Apr-2026
#-----------------------------------------------------------------------------

lst = []

while True:
  itm = input("Input Item: ")

  if itm == "!":
    break
  
  lst.append(itm)

print(lst)

lst.sort()
print(lst)

print(lst[2])
print(lst[-3])

print(lst[3:6:1])

lst.remove(lst[len(lst) - 1])
print(lst)

rmv = input("Remove Item: ")

if rmv in lst:
  lst.remove(rmv)

  print(lst)
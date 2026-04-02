#-----------------------------------------------------------------------------
# Name:        Lab-05 (Lab 05.py)
# Purpose:     Get introduced to and become familiar with Python librar(y)(ies) and its/their respective function and methods alike
#
# Author:      Brian Z.
# Created:     23-Mar-2026
# Updated:     23-Mar-2026
#-----------------------------------------------------------------------------

import math

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

if 0 <= math.pow(b, 2) - 4 * a * c:
  root1 = (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)
  root2 = (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / (2 * a)

  if root1 > root2:
    temp = round(root1, 1)
    root1 = round(root2, 1)
    root2 = temp
    
    print(f"Root: {root1}")
    print(f"Root: {root2}")
    
  elif root1 == root2:
    print(f"Root: {root1}")
    
else:
  print("No Real Roots")
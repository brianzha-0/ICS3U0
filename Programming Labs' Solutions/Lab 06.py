#-----------------------------------------------------------------------------
# Name:        Lab-06 (Lab 06.py)
# Purpose:     Delve deeper into the capabilities of functions in programming; design tailored and purposed pieces of code that can be referenced and reusable throughout bigger implications and applications
#
# Author:      Brian Z.
# Created:     25-Mar-2026
# Updated:     25-Mar-2026
#-----------------------------------------------------------------------------

def miles_to_km(distance):
  if distance < 0:
    return None

  return 1.61 * distance

def time_in_seconds(minutes, seconds):
  if minutes < 0 or seconds < 0:
    return None

  return 60 * minutes + seconds

def letter_count(word, target):
  count = 0
  
  for i in range(len(word)):
    if word[i] == target:
      count += 1
      
  return count
#-----------------------------------------------------------------------------
# Name:        Lab-07 (Lab 07.py)
# Purpose:     Put learned functions into due use and make purpose of said semantical, specific syntax apparent
#
# Author:      Brian Z.
# Created:     01-Apr-2026
# Updated:     01-Apr-2026
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
  
  for letter in word:
    if letter == target:
      count += 1
      
  return count

for i in range(1, 17, 1):
  distance = i
  converted_distance = miles_to_km(distance)
  if converted_distance != None:
    print(f"{distance} miles is equal to {converted_distance} kilometers.\nThe converted amount of distance in kilometers from miles is {converted_distance}.")
  else:
    continue

movie_length_in_minutes = 105
movie_buffer_in_seconds = 60
movie_length_in_seconds = time_in_seconds(movie_length_in_minutes, movie_buffer_in_seconds)

if movie_length_in_minutes < 120:
  print(f"Your movie of choice has a rather conventional watch time. More specifically, the amount of seconds it takes for the entire movie to play from start to finish is {movie_length_in_seconds} seconds!")

token_id = "hfda7f94hh493q85gdj7th"
original_query = 'h'
alternative_query = chr(ord(original_query) + 1)

letter_count_original = letter_count(token_id, original_query)
letter_count_alternative = letter_count(token_id, alternative_query)

if letter_count_original != None:
  print(f"There are {letter_count_original} of the letter h in the token_id.")

elif letter_count_alternative != letter_count_original:
  print(f"On the contrary, the identification hash string contains {letter_count_alternative} of the letter {alternative_query}")

else:
  print(f"Because this token_id has a total of {letter_count_original} of the letter original_query and {letter_count_alternative} of the letter alternative_query, consider regenerating a hash for a potentially improved preference of its composition of letters and enhancing overall security when using said token elsewhere apart from this program.")
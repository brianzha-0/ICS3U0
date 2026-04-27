#-----------------------------------------------------------------------------
# Name:        Lab-08 (Lab 08.py)
# Purpose:     Learn about documentation and proper commenting for possible readers/reviewers of the code to better follow and analyze it
#
# Author:      Brian Z.
# Created:     20-Apr-2026
# Updated:     27-Apr-2026
#-----------------------------------------------------------------------------

def miles_to_km(distance):
  '''
  This function takes in a value of physical distance/length and converts it to an equivalent amount of kilometers
  
  By using a constant conversion factor, the function can properly and accurately turn and return a provided quantity (length-wise) measured in miles into its corresponding number of kilometers including decimal places accordingly (to the nearest hundreth).

  Parameters
  ----------
  distance : float
    the function is designed to be able to convert any realistic/feasible (non-negative/with and only with magnitude) amount which, in this case is distance, of miles into kilometers
  
  Returns
  -------
  float
    the amount of miles converted into greater numerical amount of kilometers, since a mile is longer than a kilometer, is returned
  
  Warnings (this section is optional)
  --------
  An error that an improper data type/format of numerical value is passed into the function if the scope of the function is narrowed down and specified to accomodate a specific one/few.

  Raises
  ------
  ExceptionType
  TypeError (only if the function is defined along the lines of def miles_to_km(float: distance) -> float:)
  
  If the/a use case of the function relies on one or multiple inputs each being casted into an integer data type like so: int(input()), the function cannot be described to take in float values for sure
  '''

  # Check if the given amount of distance in miles is non-negative since any negative, even in the slightest, number multiplied by 1.61 will result in a negative result; this suggests that a direction exists and is considered which is unwanted
  if distance < 0:
    return None

  # Return the correspnding quantity of kilometers based on the received distance in miles
  return 1.61 * distance

def time_in_seconds(minutes, seconds):
  '''
  This function aims to curate the total amount of elapsed time in seconds provided the a value in minutes as well as additional seconds.
  
  In computing, time largely works in base-60 and so it is rather common knowledge that one minute equals to 60 seconds. Moreover, this is done because the function is coded to return a value in seconds. Adding the number of seconds in the amount of minutes that this function gets when it is called to another specified quantity of seconds will yield our desired "answer".

  Parameters
  ----------
  minutes : int
    a whole number that represents the first part of a request to calculate the total amount of time measured in seconds
  seconds : int
    another whole number that represents the second part of a request to calculate the total amount of time measured in seconds
  
  Returns
  -------
  int
    the accumulated quantity of seconds based on the minutes and seconds parameters is what is returned
  
  Warnings
  --------
  This function could potentially and undesirably return a float value (that is always ending in a decimal point and some amount of zeros). This is the case because the data types of when a function like this one is actually used may give a float as the data type in terms of each parameter. A float, when multiplied, by or with an integer or another float amount in Python will result in a float.

  Raises
  ------
  TypeError
  If the function is defined and defined only as def minutes_to_seconds(int: minutes, int: seconds) -> int: an error will occur where the inputted values when calling minutes_to_seconds will have an outcome of an improper/mismatched return type.
  '''

  # Avoid cases that the outlined amount of minutes and seconds are plausible and processible
  if minutes < 0 or seconds < 0:
    return None

  # Carry out the pseudocode described above to pair this method's return statment with a proper value of seconds
  return 60 * minutes + seconds

def letter_count(word, target):
  '''
  This very function is designed to count the occurances of a certain letter of the alphabet (case-specific) in a string.
  
  Taking in the string and the letter to look for allows the function to perform an iteration/one-pass over the string of individual letters/word and, with an if statement, add to a variable count appropiately in order to keep track of the appearances of that letter (which could be uppercase or lowercase as with constituents of the string itself), if any.

  Parameters
  ----------
  word : str
    while not necessarily always forming a word, the given string being passed into the function allows something to be searched before anything is even started upon
  target : chr
    this parameter serves as the motive behind even making this function to begin with; it is a letter that should be singled out when encountered whilst "reading" the word parameter above
  
  Returns
  -------
  int
    the counted quantity of times that the specified letter comes up within a string is returned promptly
  
  Warnings
  --------
  This instance of a potential caveat is that the string itself may not contain the exact "format" of the outlined target parameter. For example, the letter that is asked to be looked for could be uppercase while the string contains that letter but not in uppercase, or vice versa.

  Raises (this section is only applicable if your function raises an exception)
  ------
  N/A
    As far as the Python language goes, there is not a certain error that unfolds because of what is mentioned above.
  '''

  # Initialize a variable as zero in order to keep track of the amount of instances of a letter inside of the string
  count = 0

  # Pass over the string's letters one by one so as to check if each letter is the target one
  for letter in word:
    # The actual detailed check for the letter being present at the current letter inside of word
    if letter == target:
      # Add one to count conditionally (notice the indentation of this line) since one check can only result in at most one more occurance of the target letter
      count += 1

  # Pass back the amount of times target appeared when searching a provided string
  return count







# Here, in the main code, is an arbitrary loop with deliberately chosen parameters to showcase the things and/or (cap)abilities the corresponding function from above can perform
for i in range(1, 17, 1):
  distance = i
  converted_distance = miles_to_km(distance)
  if converted_distance != None:
    print(f"{distance} miles is equal to {converted_distance} kilometers.\nThe converted amount of distance in kilometers from miles is {converted_distance}.")
  else:
    continue

# Initialize and store a bunch of preset values produced out of personal preference to use throughout the corresponding function
movie_length_in_minutes = 105
movie_buffer_in_seconds = 60
movie_length_in_seconds = time_in_seconds(movie_length_in_minutes, movie_buffer_in_seconds)

if movie_length_in_minutes < 120:
  print(f"Your movie of choice has a rather conventional watch time. More specifically, the amount of seconds it takes for the entire movie to play from start to finish is ")

# Give values with validity within reason to variables that don't change particularly much for the sole purpose of due usage within corresponding function calls
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
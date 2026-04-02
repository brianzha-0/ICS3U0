#-----------------------------------------------------------------------------
# Name:        Lab-03 (Lab 03.py)
# Purpose:     
#
# Author:      Brian Z.
# Created:     06-Mar-2026
# Updated:     06-Mar-2026
#-----------------------------------------------------------------------------

# TASK 1
# Show in the console that two successive inputs are being sought after, specifically two numbers which represent the lower bound and upper bound of an arithmetic sequence with a common difference of 1
first_number = int(input("Input the first number of your series: "))
second_number = int(input("Input the second number of your series: "))

# Declare a numerical variable as equal to zero to keep track of the total sum of the numbers we encounter through iteration so that an error is not thrown (if the variable is merely initialized, the program cannot add to a null or unknown data type and value)
sum = 0

# Instate a loop with the purpose of iterating over numbers from the previously obtained lower bound and upper bound numbers' range, inclusive, to deduce the numbers in between and add them to the tracked total sum
for number in range(first_number, second_number + 1, 1):
  sum += number

# Check if the sum is a non-zero amount and, if so, output the stored value to the console with an appropriate message or text to accompany it as required so that the user/machine knows what the number means; otherwise, the code knows that no numbers were added to our variable in the above for loop because first_number was larger than that of second_number making the for loop invalid since our specified/default step is one 
if sum:
  print(f"Sum: {sum}")
else:
  print("Invalid")


# TASK 2
# Take in input for a number which is not a decimal in order to find the maximum number that it is divisible by
factor_number = int(input("Input a number to find the largest factor: "))

# Set two variables to track our needed result (the largest integer factor of factor_number) and an increment to serve as the complementary divisor in sequentially checking divisibility from greatest to least via mathematical operation(s)
largest_factor = 0
divisor = 2

# Our condition for the while loop to continue running is if our incremented amount is less than half of the given number since the largest possible factor of factor_number is half of itself; in other words, the smallest possible divisor into certain numbers is two, so the code should assume and start from the base case scenario of two as our divisor variable
while divisor < factor_number / 2:
  if factor_number % divisor == 0:
    # In fact, our answer will be produced on our first execution of this if statement in the case that a composite number is found
    largest_factor = factor_number // divisor
    print(f"Largest Factor: {largest_factor}")

    # If divisibility is registered as true, this line where divisor is set to a number that will, for sure, make the while loop end and software outside of it will then run
    divisor = factor_number
  else:
    # If no valid factor is yielded from 
    divisor += 1

# Allow the program to meet an exceptionary instance where no factor_number is found, and the only single "largest" factor found is one (all real numbers are divisible by it). This happening means that the inputted number is prime
if not largest_factor:
  print("Prime")
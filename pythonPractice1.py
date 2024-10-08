# Python Activity
#
# Fill in the code for the function below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.

# Part A. odd_number
# Define a function odd_number(num) that takes a number and returns True/False if the number is an odd number
def is_odd_number(num):
  return (num % 2) == 1 #True/False


# Part B. has_lowercase
# Define a function has_lowercase(s) that takes a string s
# and checks if string s contains a lower case char.
# The function should return True indicating that string s has a lower case char
# otherwise return False
def has_lowercase(string):
  for c in string:
    if c.islower():
      return True

  return False

# Part C. fizz_buzz
# Define a function fizz_buzz(num) that takes an integer num
# and returns a string based on the following criteria:

# if num is divisible by 3 return "Fizz"
# if num is divisible by 5 return "Buzz"
# if num is divisible by 3 and 5 return "FizzBuzz"

# if num is does not meet any of the above criteria or is less than
# or equal to 0 return the num as a string
def fizz_buzz(num):
  if num <= 0:
    return str(num)
  elif (num % 3 == 0) and (num % 5 == 0):
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  
  return str(num)


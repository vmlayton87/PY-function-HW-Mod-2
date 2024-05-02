# Write a Python function called rev_string() to reverse a string.

# sequence[start:stop:step]
# if nothing is entered for the start and stop they are defaulted to the beginning and end of the sequence, negative numbers reverse the sequence

def rev_string(string):
   print(string[::-1])

rev_string('hello')
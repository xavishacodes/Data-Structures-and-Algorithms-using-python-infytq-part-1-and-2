# Problem Statement
# Write a python function which searches for a particular substring in a given string. The substring may occur more than once in the string. If found, return the number of occurrences of the substring in the string. Otherwise, return 0.

 

# Perform case sensitive string comparison wherever necessary.

#lex_auth_0127667355651112963444
import re

def pattern_search(text, pattern):
    return len(re.findall(pattern,text))

#Use different values for text and pattern and test your program
text = "MESMERIZING MESSAGE"
pattern = "MES"
result=pattern_search(text, pattern)
print("The given text:",text)
print("Pattern:",pattern)
print("No. of occurrences of the pattern :",result)
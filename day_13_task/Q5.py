# Write a Python program to match a string that contains only uppercase letters
## Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
def regexx(string):
    charRe = re.compile(r'[^A-Z]')
    string = charRe.search(string)
    return not bool(string)

print(regexx("ABCDEF")) 
print(regexx("*&%@#!}{"))
print(regexx("A"))
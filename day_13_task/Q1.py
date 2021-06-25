## Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
def regexx(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(regexx("ABCDEFabcdef123450")) 
print(regexx("*&%@#!}{"))
print(regexx("Aa1"))
#Write a Python program to check for a number at the end of a word/sentence.
import re

mch = "hello best enlist6"
x =re.findall("\w+\S*$",mch)
print(x)
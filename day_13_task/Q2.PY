#  Write a Python program that matches a word containing 'ab'.
import re

mch = "hello i am capable of  writing"
x =re.findall("ab",mch)
print(x)

x =re.search("ab",mch)
print(x)

x =re.split("ab",mch)
print(x)

x =re.sub("ab","AB",mch)
print(x)

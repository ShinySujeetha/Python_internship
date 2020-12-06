#special set of characters
import re
x=input("Enter a text")
Char=re.compile("[a-zA-Z0-9]+")
if Char.fullmatch(x) is None:
    print("Only certain special characters")
else:
    print("Has special characters")
print()
print()
#Match a word containing 'ab'
a=str(input("Enter a string"))
if re.search("ab",a):
    print("Match found")
else:
    print("Match not found")
print()
print()
#Checking number at the end of a word/sentence
b=input("Enter a text")
if re.search("[0-9]$",b):
    print("Number found at end")
else:
    print("Number not found at the end")
print()
print()
#Searching numbers (0-9) of len btn 1 to 3 in a string
c=input("Enter a text")
num=re.finditer(r"([0-9]{1,3})",c)
for i in num:
    print(i.group(0))
print()
print()
#Match a string that contains only uppercase
y=input("Enter a text")
char=re.compile("[A-Z]+")
if char.fullmatch(y) is None:
    print("No match")
else:
    print("Match found")

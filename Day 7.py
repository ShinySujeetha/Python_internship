#Creating a python module with list and importing the module in another.py file and changing the values in list
from List import List
new_List=[2,3,4,5,6]
List=new_List
print(List)
print()
print()
#Importing a module that picks random number and to fetch a random number from 1 to 100
import random
print("Random number from 1 to 100:",random.randint(1,100))


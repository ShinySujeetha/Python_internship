List=[2,35,49,32,12,97]
for i in  List:
    print(i+2)
    
print()    
print("54321 series:")
    
for i in range(0, 5):
    for j in range(5, i, -1):
        print(j, end="")
    print()
    
print()
print("Finonacci series:")
    
n=int(input("Enter the no.of terms:"))
n1,n2=0,1
if n<=0:
    print("Enter a positive number")
elif n==1:
    print(n1)
else:
    for i in range(0,n,1):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
print()        

print("To check if its an Armstrong number:")
        
n=int(input("Enter a number:"))
sum=0
a=n
while(a>0):
    b=a%10
    sum += b**3
    a //= 10
if n==sum:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
print()

print("Multiplication table of 9")
for i in range(1,21,1):
    print("9 x ",i,"=",i*9)
print()

print("To check positive or negative:")

n=int(input("Enter a number:"))
if(n<0):
    print("Negative number")
elif(n==0):
    print("Neither positive nor negative")
else:
    print("Positive number")
print()

print("To convert the number of days to age:")

n=int(input("Enter the no.of days"))
y=n/365
print("The age is:",int(y))
print()

print("Trignometric function:")

import math
n=float(input("Enter a value:"))
print("cos(",n,")=",math.cos(n))
print("sin(",n,")=",math.sin(n))
print()

print("Calculator on a code level for basic arithmetic operations:")

def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def divide(x, y): 
      return x / y  
print("Select operation.")  
print("1.Add")  
print("2.Subtract")  
print("3.Multiply")  
print("4.Divide")  
  
choice = input("Enter choice(1/2/3/4):")  
  
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
  
if choice == '1':  
   print(num1,"+",num2,"=", add(num1,num2))  
  
elif choice == '2':  
   print(num1,"-",num2,"=", subtract(num1,num2))  
  
elif choice == '3':  
   print(num1,"*",num2,"=", multiply(num1,num2))  
elif choice == '4':  
   print(num1,"/",num2,"=", divide(num1,num2))  
else:  
   print("Invalid input")  



    

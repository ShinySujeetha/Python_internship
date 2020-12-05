def add(x, y):  
   return x + y 
def subtract(x, y): 
   return x - y 
def multiply(x, y): 
   return x * y 
def division(x,y):
    try:
        result = x / y
        print(result)
    except Exception as e:
        print(e)
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
   print(num1,"/",num2,"=", division(num1,num2))  
else:  
   print("Invalid input")  
print()
print()
try:
    print(x)
except NameError:
  print("Variable is not defined")
except:
  print("Invalid")
print()
print()
try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')


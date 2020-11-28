a=int(input("Number1:"))
b=int(input("Number2:"))

def math(x,y):
    print("Addition of two numbers is",a+b)
    print("Subtraction of two numbers is",a-b)
    print("Multiplication of two numbers is",a*b)
    print("Division of two numbers is",a/b)
    
print(math(a,b))

def covid(patient_name,body_temp=98):
    print("The patient name is ",patient_name)
    print("The body temperature is ",body_temp," degrees")

print(covid(input("Enter patient name")))

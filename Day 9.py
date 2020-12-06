#multiply arg x with arg y
a=lambda x,y:x*y
print(a(6,7))
print()
print()
#creating a fibonacci series using lambda
from functools import reduce
fib=lambda n:reduce(lambda x, _:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(fib(5))
print()
print()
#Multiplying the elements in the list with a given value
list1=[1,2,3,4]
x=int(input("Enter a number"))
result=list(map(lambda n: n*x,list1))
print(result)
print()
print()
#Numbers divisble by 9
List=[82,65,9,33,45,80,63,7]
mul_9=list(filter(lambda n:n%9==0,List))
print(mul_9)
print()
print()
#Counting even numbers in the list
List2=[3,5,6,8,9,21,3,4,22,30]
even=len(list(filter(lambda n: n%2==0,List2)))
print(even)
         

Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> List=[37,28,4857,20,19,27,7,46]
>>> List.append(55)
>>> print(List)
[37, 28, 4857, 20, 19, 27, 7, 46, 55]
>>> List.remove(20)
>>> print(List)
[37, 28, 4857, 19, 27, 7, 46, 55]
>>> print(max(List))
4857
>>> print(min(List))
7
>>> Tup=(29,18,46,39,"Hi",8.47,90,"Hello")
>>> new_Tup=tuple(reversed(Tup))
>>> print(new_Tup)
('Hello', 90, 8.47, 'Hi', 39, 46, 18, 29)
>>> print(list(Tup))
[29, 18, 46, 39, 'Hi', 8.47, 90, 'Hello']
>>> 
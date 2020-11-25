Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={"Maths":90,"English":75,"Science":80}
>>> dict2={"Apples":"Red","Pear":"Green","Grapes":"Violet"}
>>> new_dict=dict1.copy()
>>> new_dict.update(dict2)
>>> print(new_dict)
{'Maths': 90, 'English': 75, 'Science': 80, 'Apples': 'Red', 'Pear': 'Green', 'Grapes': 'Violet'}
>>> print(dict2.pop("Grapes"))
Violet
>>> print(dict2)
{'Apples': 'Red', 'Pear': 'Green'}
>>> Subject=['Maths','English','Science']
>>> Marks=[90,75,80]
>>> Result=dict(zip(Subject,Marks))
>>> print(Result)
{'Maths': 90, 'English': 75, 'Science': 80}
>>> Set1={12,32,41,25,63,10,98,02,58}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> Set1={12,32,41,25,63,10,98,2,58}
>>> print(len(Set1))
9
>>> Set1={1,2,3,6,4,3,5,2,6,7,5,3,5,9}
>>> Set2={4,6,7,4,6,8,5,6,8,}
>>> print(Set1-Set2)
{1, 2, 3, 9}
>>> 
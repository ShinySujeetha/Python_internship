Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(dir(locals()['__builtins__']))
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>>  print "Hello"
 
SyntaxError: unexpected indent
>>> L1=[1,2,3]
>>> L1[6]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    L1[6]
IndexError: list index out of range
>>> D1={'1':"aa", '2':"bb", '3':"cc"}
>>> D1['4']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    D1['4']
KeyError: '4'
>>> import notamodule
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    import notamodule
ModuleNotFoundError: No module named 'notamodule'
>>> from math import cube
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    from math import cube
ImportError: cannot import name 'cube' from 'math' (unknown location)
>>> '2'+2
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    '2'+2
TypeError: can only concatenate str (not "int") to str
>>> int('xyz')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int('xyz')
ValueError: invalid literal for int() with base 10: 'xyz'
>>> age
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    age
NameError: name 'age' is not defined
>>> x=100/0
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x=100/0
ZeroDivisionError: division by zero
>>> 
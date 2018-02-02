Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #list
>>> easy_as =['mca',123]
>>> easy_as
['mca', 123]
>>> mca =[rishabh,24,easy_as]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mca =[rishabh,24,easy_as]
NameError: name 'rishabh' is not defined
>>> mca =['rishabh',24,easy_as]
>>> mca
['rishabh', 24, ['mca', 123]]
>>> mca.append('mca1')
>>> mca1
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    mca1
NameError: name 'mca1' is not defined
>>> mca.append('mca1')
>>> mca
['rishabh', 24, ['mca', 123], 'mca1', 'mca1']
>>> empty=[]
>>> empty.append('rishabh')
>>> empty
['rishabh']
>>> mca[-2]
'mca1'
>>> mca[1;-1]
SyntaxError: invalid syntax
>>> mca[1:-1]
[24, ['mca', 123], 'mca1']
>>> x=[letters,numbers]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x=[letters,numbers]
NameError: name 'letters' is not defined
>>> x = [letters,numbers]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    x = [letters,numbers]
NameError: name 'letters' is not defined
>>> x=[['a','b','c'],[1,2,3]]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0][1]
'b'
>>> len(x)
2
>>> len(python)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    len(python)
NameError: name 'python' is not defined
>>> 'i'

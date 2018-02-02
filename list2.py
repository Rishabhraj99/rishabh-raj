Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> country =['india',1,'afg',2]
>>> country
['india', 1, 'afg', 2]
>>> len(country)
4
>>> list1=[1,2,3,4,5,6,7,8,9,'rishabh','himanshu']
>>> list1
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'rishabh', 'himanshu']
>>> list[:10]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list[:10]
TypeError: 'type' object is not subscriptable
>>> list[ : 8]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    list[ : 8]
TypeError: 'type' object is not subscriptable
>>> list[1:2]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list[1:2]
TypeError: 'type' object is not subscriptable
>>> list1[:8]
[1, 2, 3, 4, 5, 6, 7, 8]
>>> list1[1:9]
[2, 3, 4, 5, 6, 7, 8, 9]
>>> list1[:3]
[1, 2, 3]
>>> list1[1:2:3]
[2]
>>> list[2:3:4]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    list[2:3:4]
TypeError: 'type' object is not subscriptable
>>> list1[2:3:4]
[3]
>>> list1[1:2:8]
[2]
>>> list1[1:8:2]
[2, 4, 6, 8]
>>> #1st 1 is starting number.8 is last number..2 is space
>>> list2=[2,3,4,5,2,6,7,8,9]
>>> list1+list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'rishabh', 'himanshu', 2, 3, 4, 5, 2, 6, 7, 8, 9]
>>> list1-list2
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list1-list2
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> list4=[3+3,4+5,4*5,5/2]
>>> list4
[6, 9, 20, 2.5]
>>> 

Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students = "John, Mary, Steve"
>>> students = ["John", "Mary","Steve"]
>>> type(Students)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    type(Students)
NameError: name 'Students' is not defined
>>> type(students)
<class 'list'>
>>> len(students)
3
>>> students[0]
'John'
>>> students[2]
'Steve'
>>> students[0:1]
['John']
>>> students[1]
'Mary'
>>> students[:1]
['John']
>>> students[:2]
['John', 'Mary']
>>> students[-1]
'Steve'
>>> students[:2]
['John', 'Mary']
>>> months = ("January", "February", "March")
>>> type(months)
<class 'tuple'>
>>> months[0]
'January'
>>> months[-1]
'March'
>>> students[0] = "Geogre"
>>> students
['Geogre', 'Mary', 'Steve']
>>> months[0] = "new month"
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    months[0] = "new month"
TypeError: 'tuple' object does not support item assignment
>>> students.append("Kate")
>>> students
['Geogre', 'Mary', 'Steve', 'Kate']
>>> students.insert(0, "Peter")
>>> students.pop()
'Kate'
>>> students
['Peter', 'Geogre', 'Mary', 'Steve']
>>> students.pop(1)
'Geogre'
>>> students
['Peter', 'Mary', 'Steve']
>>> students.remove("Mary")
>>> students
['Peter', 'Steve']
>>> students2 = ["Paul", "John"]
>>> students + students2
['Peter', 'Steve', 'Paul', 'John']
>>> 
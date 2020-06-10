Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> person = ["John", "Green", "1980", "Canada"]
>>> person = {"first_name":"John","last_name":"Green","birth_year":1980,"country_of_birth":Canada}
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    person = {"first_name":"John","last_name":"Green","birth_year":1980,"country_of_birth":Canada}
NameError: name 'Canada' is not defined
>>> person = {"first_name":"John","last_name":"Green","birth_year":1980,"country_of_birth":"Canada"}
>>> person["first_name"]
'John'
>>> person["birth_year"] = 1979
>>> person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada'}
>>> person["marital_status"] = "Married"
>>> person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married'}
>>> person["children']=["Nathalie","Etha"]
       
SyntaxError: invalid syntax
>>> person["children"]=["Nathalie","Etha"]
>>> person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Nathalie', 'Etha']}
>>> person["children"].append("anna")
>>> person
{'first_name': 'John', 'last_name': 'Green', 'birth_year': 1979, 'country_of_birth': 'Canada', 'marital_status': 'Married', 'children': ['Nathalie', 'Etha', 'anna']}
>>> person["age"]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    person["age"]
KeyError: 'age'
>>> person.get("age")
>>> person.get("age","invalid property")
'invalid property'
>>> person.get("children","invalid property")
['Nathalie', 'Etha', 'anna']
>>> Key = "first_name"
>>> person[Key]
'John'
>>> person["first_name"]
'John'
>>> person.clear()
>>> person
{}
>>> 
= RESTART: C:/Users/Sai Ganesh/Desktop/Python Training/Section 2/Dictionaries Exercise.py
What would you like to know about the person?name
Peter
>>> 
= RESTART: C:/Users/Sai Ganesh/Desktop/Python Training/Section 2/Dictionaries Exercise.py
What would you like to know about the person?blah
invalid property
>>> 
= RESTART: C:/Users/Sai Ganesh/Desktop/Python Training/Section 2/Dictionaries Exercise.py
What would you like to know about the person?Name
Peter
>>> 
code.py

import datetime

class employee:
    
    num_of_emps = 0
    raise_amount = 1.04
     
    def __init__(self, first, last, pay): #what is the purpose of constructor / see notes
        self.first = first
        self.last = last
        self.pay = pay
        
        employee.num_of_emps += 1

    @property  
    def email(self):
        return f'{self.first}.{self.last}@company.com'  

    @property
    def fullname(self): #will get error without self instance
        return f'{self.first} {self.last}'  
    
    @fullname.setter 
    #when changing fullname in the code below. It comes to this setter and parsed the names and set the first and last names again
    def fullname(self, name): 
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #how are we able to access it through self
        
        #self.raise_amount is preferred over employee.raise_amount as you will be able to change for any single employee if needed.
        #any subclass can override that constant

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod #what are methods ? /see notes
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class developer(employee): #Inherits all of the Employee class methods. What is inheritance/ see notes
    raise_amt = 1.10 #this applies for developer class and employee class will be different

    def __init__(self, first, last, pay, prog_lang): 
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class manager(employee):

    def __init__(self, first, last, pay, employees = None): 
    #when setting a default value for an ungiven argument, avoid using an empty mutable data type.
    #This is why employees = None in arguments instead of [] - Reason yet to be explained. 
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())



dev_1  = developer('Sai', 'Ganesh', '50000', 'Python')
dev_2 = developer('Test', 'User', '60000'. 'Java')

mgr_1 = manager('Sue', 'Smith', 90000, [dev_1])

print(dev_1.email)
print(dev_1.prog_lang)

print(dev_1.pay)
dev_1.apply_raise #will use 1.10 but employee class remains as before
print(dev_1.pay)

print(mgr_1.email)

emp_1 = employee('Sai', 'Ganesh', '50000')
emp_2 = employee('Test', 'User', '60000')

#different ways to call 
print(employee.fullname(emp_1)) #have to pass it an instance
print(emp_1.fullname()) #do not need to pass it an instance

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = employee.from_string(emp_str_1)

my_date = datetime.date(2016, 7, 10) #A suggestion we can use datetime module to get current date
print(employee.is_workday(my_date))

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
print(mgr_1.print_emps())

# This method returns the boolean value of whether an instance belongs to a class. Useful when using inheritance
print(isinstance(mgr_1, manager))
print(isinstance(mgr_1, employee))

#.issubclass(subclass, class)
#This method returns the boolean value of whether a class has inherited from the second class.

print(issubclass(manager, employee))
print(issubclass(manager, developer))


#The below codes make use of special methods.  
print(emp_1)
print(repr(emp_1))
print(str(emp_1))

def __repr__(self):
    return "Employee(f'{self.first}, {self.last}, {self.pay}')"

def __str__(self):
    return f'{self.fullname()} - {self.email}'  

print(emp_1.__repr__)
print(emp_1.__str__)


def __add__(self, other): #check documentation for other types of special methods like this
    return self.pay + other.pay 
print(emp_1 + emp_2)


# After property decorator added 
emp_test = employee('John'. 'Smith')
emp_test.first = 'Jim'

print(emp_1.email) 
print(emp_1.fullname) #parantheses removed after property decorator 


#After setter included:

emp.fullname = 'Sai Ganesh'
print(emp_1.fullname) #will give error this requires a setter.




print(1+2)
#This actually makes use of a special method / see below:
print(int.__add__(1, 2))
#Another example:
print('a'+ 'b')
print(str.__add__('a', 'b'))


# len is also an example of dunder method
#Normally:
print(len('test'))

def __len__(self):
    return len(self, fullname())

print('test'.__len__())
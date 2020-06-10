# This OOP File was done with reference to lessons from Corey Schafer Youtube Channel. 

import datetime

class employee:
    
    num_of_emps = 0
    raise_amount = 1.04
     
    def __init__(self, first, last, pay): #what is the purpose of constructor / see below
        self.first = first
        self.last = last
        self.pay = pay
        
        employee.num_of_emps += 1
    
    #Purpose of Constructor: 

    """ Without constructor function (also known as __init__)
    emp_1 = employee()
    emp_2 = employee()

    emp_1.first = 'Sai'
    emp_1.last = 'Ganesh'
    emp_1.email = 'Sai.Ganesh@company.com'
    emp_1.pay = 50000


    emp_2.first = 'Test'
    emp_2.last = 'User'
    emp_2.email = 'Test.User@company.com'
    emp_2.pay = 60000
    """

    @property  
    def email(self):
        return f'{self.first}.{self.last}@company.com'  

    @property
    def fullname(self): #well get error without self instance
        return f'{self.first} {self.last}'  
    
    @fullname.setter #when changing fullname in the code below. It comes to this setter and parsed the names and set the first and last names again
    def fullname(self, name): 
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!')
        self.first = None
        self.last = None


#Initial constructor before property decorator  
"""
Setters, getters and deleters are examples of property decorators. 
Setters and getters and deleters are useful for avoiding massive changes in codes. 
If these are added, just a single line below is required, instead of having to add/remove parantheses etc. 

    def __init__(self, first, last, pay): 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        employee.num_of_emps += 1
    
    
    emp_test = employee('John'. 'Smith')
    emp_test.first = 'Jim'

    print(emp_1.email) #this still is John as email is defined in the constructor function as the full name initially assigned. 
    print(emp_1.fullname())  #full name method doesn't have the  takes the current first name and last name
    #First solution you think of is to create a email method. Instead as above property decorator

    # So if function added case:
    def __init__(self, first, last, pay): 
        self.first = first
        self.last = last
        self.pay = pay
        
        employee.num_of_emps += 1
    

    def email(self):
        return f'{self.first}.{self.last}@company.com'   
    
    emp_test = employee('John'. 'Smith')
    emp_test.first = 'Jim'

    print(emp_1.email()) #This requires a change code as additional parantheses are required. Instead can add property decorator as above
    print(emp_1.fullname())  


"""

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #how are we able to access it through self
        #self.raise_amount is preferred over employee.raise_amount as you will be able to change for any single employee if needed.
        #any subclass can override that constant

#How are we able to access raise_amount from self instance if it is not defined in the constructor function:

"""
____________________________________________________________________________________________________________________________

Class variables are variables that we set inside a class, and are shared among all instances

Instance variables are variables that are different from each instance.
"""

"""
print(employee.raise_amount)  ## All give 1.04
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__) #raise_amount not within this dict
print(employee.__dict__) #raise_amount is within this dict

Employee.raise_amount = 1.05

print(employee.raise_amount)  ## All give 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.06

print(employee.raise_amount)  ## only emp_1 gives 1.06 , rest gives 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__) #now raise amount of 1.06 will be within this dict as the 1.06 is specific to emp_1 and not to the class itself



print(employee.num_of_emps) #returns 2 as we have emp_1 and emp_2
"""
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod #what are methods ? /see below
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
#What are the different types of methods?

"""
_______________________________________________________________________________________________________________________________________
Firstly, a regular method is the type of method that we are used to seeing from the first few codes.
It is accessible through both the class and the instance, which means that we can call for the method in both

Employee.method()

&

emp_1.method()

they automatically have the instance as the first positional argument, as self.

_______________________________________________________________________________________________________________________________________


Secondly, class methods are the type of method used when a method is not really about an instance of a class, but the class itself.
To create a class method, just add '@classmethod' a line before creating the class method. 
The class is automatically the first argument to be passed in, and is represented as 'cls' instead of 'class'. 
This is because 'class' is already assigned to be something else in Python. 
There are 2 ways of using the class method.

First is modifying the class variable. 
Modified the 'raise_amount' class variable using a class method. 
Just remember that to access a class variable, we have to write 'cls.' before specifying the actual name. 
For example, as 'cls.raise_amount' as above.


Second is making an alternative constructor. 
Sometimes people have information of their specific instances of the class available in a specific format. 
Above there is an example of this where first and last names and pay are separated by a hyphen. 
In the above code, we created a class method that returns the class with the specific values passed in 
that are obtained by using split() method to the string passed in. 

User of the script can now automatically create a new instance without having to parse the string at '-'.
______________________________________________________________________________________________________________________________________

Static methods are different from regular methods and class methods. 
In static methods it doesn't have a class or instance that is automatically passed in as a first positional argument. 
They can be created by adding '@staticmethod' a line before defining the method. 
These are methods that have a logical connection to the Class, but does not need a class or instance as an argument. 
It is better to make sure we create a static method rather then class or regular method when 
we are sure that we don't make use of the class or instance within the method.


"""
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class developer(employee): #Inherits all of the Employee class methods. What is inheritance/ see below:
    raise_amt = 1.10 #this applies for developer class and employee class will be different
"""
_______________________________________________________________________________________________________________________________________
1. What is inheritence?
It is a method that allows us to create a new class that shares the same attributes and method with the original function, 
and add some extra functionality to the new class. It also does not disturb the original class.


2. How to make a class inherit from another class?
class Developer(Employee):


3. Structure of classes and subclasses.
When we input a function to a subclass, python follows the 'method resolution order', 
which is the chain of classes that it goes through to find what the method is. 
All classes have the built-in group of methods and attributes as their primary order.


4. How to initiate the subclass so that it can handle more information than its original class can?
There are 2 ways.
first, using the super method as follows and pass in the arguments in interest.
super().__init__()


Second, call the parent's init method explicitly and pass in the arguments in interest.
Employee.init(self, first, last, )


5. Useful tools when exploring the inheritance system.
.isinstance(instance, class)
This method returns the boolean value of whether an instance belongs to a calss
.issubclass(subclass, class)
This method returns the boolean value of whether a class has inherited from the second class.


6. Example of class inheritance
Whisky library 

++ . .
________________________________________________________________________________________________________________________________
"""
    def __init__(self, first, last, pay, prog_lang): 
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class manager(employee):

    def __init__(self, first, last, pay, employees = None): 
    #when setting a default value for an ungiven argument, avoid using an empty mutable data type.
    #This is why employees = None in arguments instead of []
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

print(1+2)
#This actually makes use of a special method / see below:
print(int.__add__(1, 2))
#Another example:
print('a'+ 'b')
print(str.__add__('a', 'b'))


def __add__(self, other): #check documentation for other types of special methods like this
    return self.pay + other.pay 
print(emp_1 + emp_2)




# len is also an example of dunder method
#Normally:
print(len('test'))

def __len__(self):
    return len(self, fullname())

print('test'.__len__())


"""
Special Methods a.k.a Magic methods allows us to emulate some built-in behaviour within python and it is also how we implement operator
overloading. What does operator overloading mean?

print(1 + 2) 

vs

print('a' + 'b')

By defining special methods,

we will be able to change some of this built in behaviour and operations. These special methods are surrounded by double underscores(dunder)
 e.g. __init__ (dunder init)  - this sets all the attributes for us. Check constructor function notes above to understand more. 

 2 more common special methods:

 __repr__

 __str__


 #Example Practical
#Datetime module

#++ return NotImplemented
"""




# After property decorator added 
emp_test = employee('John'. 'Smith')
emp_test.first = 'Jim'

print(emp_1.email) 
print(emp_1.fullname) #parantheses removed after property decorator 


#After setter included:

emp.fullname = 'Sai Ganesh'
print(emp_1.fullname) #will give error this requires a setter.

#After Deleter Added
del emp_1.fullname











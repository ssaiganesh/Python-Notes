#Data may be associated with class or object

class Animal:
    #__init__  method is constructor
    #within __init__ method, initialising 3 variable type, name and sound
    # those are object variables. 
    # only exist when object is created from classs
    
    x= [1,2,3] #this is a class variable not object variable as defined under class and not method
    #Refer below to the encapsulation for this variable x
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    #setters and getters is one of the principles of encapsulation
    #You never access these variables directly.
    #That is why we have the underscore in front of them
    #In many langauges there is a concept of private variables
    #that simply cannot be accessed or changed from outside of class definition
    #Python doesn't have that
    #Instead we have a convention, the convention is to use this underscore and that means
    #do not touch this. SO you never want to set that directly from outside of class methods


    #Fuctions below are getters and setters
    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    #Reading it in string function, reading it using getter because it's safe
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    ##ao._name = "Joe" # DO NOT DO THIS _ is private only within method function
    print(a0)
    print(a1)

    print(a0.x)
    a1.x[0] = 7
    print(a0.x) #interesting a0 has changed as well. This is because 
    
    """
    this variable x is only associated with the class and only exists in the class
    The object doesn't have this variable x and it is drawing it from the class not from the object
    That is a very important distinction
    This comes to something called encapsulation
    Encapsulation is one of the major benefits of object oriented programming
    If my variables are encapsulated, that means that they belong to the object and not to the class
    The x variable is not encapsulated and so it exists
    It is exactly the same object in every instance of the class
    And every object that is created by the class because it only exists in the class
    That makes it not encapsulated.
    As a general rule, except for things like constants that your are never going to change
    and those should be immutable not mutable. You are never going to want to put mutable data in the class
    
    """

if __name__ == '__main__': main()

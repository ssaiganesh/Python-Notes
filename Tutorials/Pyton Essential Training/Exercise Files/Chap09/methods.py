#function associated with a class is called a method
#it provides interface to the class and its objects

#methods are primary interface for classes and objects.
#They work exactly like functionss, except they are bound to the object
#through their first argument, commonly named self


#object variables are named with a leading underscore
#traditional method. Python doesn't have private variables and so there is no way to prevent 
#somebody from using these. It indicates it is a private vairable 
#and it should not be set or retrieved outside of the setter getter.. referencing __type
class Animal:
    #constructor __init__
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    #this is a getter setter
    #first argument to the function is self and that's wahat makes this a method and not just a plain function
    def type(self, t = None): #t has default value of none
        if t: self._type = t #_type is private variable and cannot be retrieved outside the setter getter
        #if there is no value, or if it's none, then this if statement will fail and it will just reutnr the value of type
        return self._type
        #if there is a value then it will go ahead and it will set type before returning it

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    #specially named method 
    #special method names under documentation (under data model)
    #provides string representation of the object
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    a0.sound('bark') #set variable using setter getter funciton changes from rwar to bark
    print(a0)
    print(a1)

if __name__ == '__main__': main()

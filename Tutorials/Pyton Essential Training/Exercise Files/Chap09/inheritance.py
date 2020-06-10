#class inherticane is funadamental. Allows you to extend your classes by
#driving properties and methods from parent classes

class Animal:
    #init method no longer providing any default values
    #because it is now just base class. Going to be iherited in order to be used
    def __init__(self, **kwargs):
        if 'type' in kwargs: self._type = kwargs['type']
        if 'name' in kwargs: self._name = kwargs['name']
        if 'sound' in kwargs: self._sound = kwargs['sound']

    #because init is just base class, we need to check if value is actually there
    #this is the purpose of exceptions-- covered in later chapter
    def type(self, t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None
    #attempts to return the value and if that fails will return none

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

    #so to use this Animals class, we are now inhertiing it to create other classes

class Duck(Animal):
    def __init__(self, **kwargs):
        self._type = 'duck'
        if 'type' in kwargs: del kwargs['type'] #if there is atype in the keywrod arguments and if so, we delete that
        super().__init__(**kwargs) #through super function, call parent class initializer with our kwargs
        #super always calls the parent class

class Kitten(Animal):

    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs) 
    
    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}".')

def main():
    a0 = Kitten(name = 'fluffy', sound = 'rwar')
    a1 = Duck(name = 'donald', sound = 'quack')
    print_animal(a0)
    print_animal(a1)
    a0.kill('humans')
if __name__ == '__main__': main()


#you can also extend built in classes, because in Python everything is an object
#refer to string.py
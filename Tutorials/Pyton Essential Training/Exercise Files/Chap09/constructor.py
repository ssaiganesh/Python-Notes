#an instance of a class is called an object
#it is created by calling the class itself as if it were a function

class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'rawr'
##the if else part is giving the kwargs default values
    """
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    """
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))

"""
this is before kwargs:

def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    #can just print directly instead of initialising variable like a0 or a1:
    print_animal(Animal('velociraptor', 'veronica', 'hello'))
"""

#this is after kwargs:
def main():
    a0 = Animal(type='kitten', name='fluffy', sound='rwar')
    a1 = Animal(type='duck', name='donald', sound='quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal(type='velociraptor', name='veronica', sound='hello'))
    print_animal(Animal()) #this gives default value

if __name__ == '__main__': main()

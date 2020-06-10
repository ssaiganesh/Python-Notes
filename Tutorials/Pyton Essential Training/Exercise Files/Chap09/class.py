#everything is an object in python 
#and a class is how an object is defined

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self): #first parameter of a method is always self
        #when an object is created from the class
        #self will reference that object
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    #not recommened but can do this as well: print(donald.sound)
    donald.move()

if __name__ == '__main__': main()

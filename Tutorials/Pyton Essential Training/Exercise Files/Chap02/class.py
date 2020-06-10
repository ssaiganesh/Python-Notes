

class Duck: #within class there are functions. Duck is the name of the class in this case. 
    sound = 'Quaaaaack!'
    walking = 'Walking like a duck.'
   
    def quack(self): #first argument for a function inside a class is ALWAYS self. 
       print(self.sound)
       
    def walk(self):
        print(self.walking)

def main():
    donald = Duck() #donald is now an object of the class duck
    donald.quack() #referencing members of object donald
    donald.walk() # "" 

if __name__ == '__main__': main()

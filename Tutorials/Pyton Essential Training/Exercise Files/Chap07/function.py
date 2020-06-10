"""

def main():
    kitten()

def kitten():
    print('Meow.')

if __name__ == '__main__': main() #search up more on this
#but should be covered in modules

"""
"""
def main():
    kitten(5,6,7) #the values within function is an argument

def kitten(a,b,c):
    print('Meow.')
    print(a,b,c)

if __name__ == '__main__': main() #search up more on this
#but should be covered in modules

"""
"""
def main():
    x = [5]
    y = x
    y[0] = 3
    print(x) #take note that x is also equal to [3]
    print(y)

main()
"""

def main():
    x = [5]
    kitten(x)
    print(f'in main: x is {x}') #this will be 3

def kitten(a):
    a[0] = 3
    print('Meow.')
    print(a) # 3

if __name__ == '__main__': main()


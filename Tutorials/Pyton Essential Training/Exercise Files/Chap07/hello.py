#everything is comments as cannot define f1 or f2.. multiple times

print('Hello, World.')


def f1():
    print('this is f1')

x = f1
x()
"""
def f1():
    def f2():
        print('this is f2')
    return f2

x = f1
x()  # will give output of f1()


# f2() cannot call f2 directly will get NameError
# because f2 only exists within the scope of f1

def f1(f):
    def f2():
        print('this is before the funciton call')
        f()
        print('this is after the functoin call')
    return f2

def f3():
    print('this is f3')

x = f1(f3)
x()  #return value



#here it where it becomes decorator:

f3 = f1(f3)
f3() #wrapper

#there is a shortcut for the above steps:

def f1(f):
    def f2():
        print('this is before the funciton call')
        f()
        print('this is after the functoin call')
    return f2

@f1 #decorator function
def f3():
    print('this is f3')

f3()


@ 
this syntax here is called the decorator 
it takes the function directly after it. In this case f3
and it passes the function as an argument to the decorator function
and it returns and assigns that name of f3 to the wrapper itself

now f3 cannot be called directly. it is wrapped inside the decorator function
see the usefulness in the decorator.py file
"""
"""
a generator is a special class of function that serves
as an iterator instead of returning a single value the 
generatore returns a stream of values.
"""

def main():
    for i in inclusive_range(25): #Function created below. 0 up to 25 unlike range. which will only be upto 24
        print(i, end = ' ')
    print()

def inclusive_range(*args): #variable argument list
    numargs = len(args) #number of args is the length
    start = 0 #initialising variable
    step = 1   #initialising another variable
    
    # initialize parameters
    #very similar to range where there is start,stop,step or just stop, or start & stop only
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start #initialise i
    while i <= stop: #using while loop
        yield i #yield is like return but used for generator
        #yield a value and function continues until yields next value
        i += step

if __name__ == '__main__': main()

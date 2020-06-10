

def main():
    x = ('meow', 'grrr', 'purr')
    kitten(*x) #explanation for asteriks given below

def kitten(*args): #*args is the variable length argument list. WE can treat it like a sequence, it is actually a tuple
    #traditional to name list args 
    if len(args): #means if this is true otherwise aka length is greater than zerp
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()

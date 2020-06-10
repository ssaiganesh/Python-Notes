

def main():
    x = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr') 
    kitten(**x)    
    #kitten(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr') #same as dictionary

def kitten(**kwargs): #kwargs stands for key word arguments
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} says {}'.format(k, kwargs[k]))
    else: print('Meow.')

if __name__ == '__main__': main()

#check kwargs vs args
# *args vs **kwargs



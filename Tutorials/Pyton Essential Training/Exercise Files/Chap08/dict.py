#dictionary type is a hashed key value structure. Comparable to associative arrays 
#in other lanaguages

def main():
    """
    #This is a dictionary. A clearer and alternate method is shown after this
    animals = {'kitten': 'meow', 'puppy':  'ruff!', 'lion': 'grrr', 
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' )
    """

    #with dict function:
    animals = dict(kitten = 'meow', puppy =  'ruff!', lion = 'grrr', 
        giraffe = 'I am a giraffe!', dragon = 'rawr' )
    for k , v in animals.items(): print(f'{k}: {v}')
    print_dict(animals)  #function carries out the above line of code
    # to get only keys from the above dictionary
    for k in animals.keys(): print(k)
    # To get only values from the above dictionary:
    for v in animals.values(): print(v)
    #to get value of specific key:
    print(animals['lion'])
    #mutable so can change also
    animals['monkey'] = 'haha'
    
    
    

#key-value pairs are within the dictionary


def print_dict(o): #function prints the dictionary in nice readable format
    for k , v in o.items():  print(f'{k}: {v}')

if __name__ == '__main__': main()


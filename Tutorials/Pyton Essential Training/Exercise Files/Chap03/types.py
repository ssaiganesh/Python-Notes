

x = 7
print('x is {}'.format(x))
print(type(x))

y = 'seven' #string type 
print('y is {}'.format(y))
print(type(y))

y = 'seven'.capitalize() #changes seven to Seven (only first letter)

y = 'seven'.upper() # changes seven to SEVEN

y = 'seven'.lower() #changes characters to lower case. in this case no change

z  = '''

seven 

'''  #multi-line string  or can be """ instead of ''' as well


print('z is {}'.format(z))
print(type(z))


w  = 'seven {} {}'.format(8,9)
print('w is {}'.format(w))
#this returns output: w is seven 8 9

#an alternative for the above:
a  = 8
b = 9
w = f'seven {a} {b}' #pros of f-strings
print('w is {}'.format(w))


a  = 'seven {1:<9} {0:>9}'.format(8,9) #left align and right align 9 spaces
print('a is {}'.format(a))


b = '"seven {1:<9} {0:>9}"'.format(8,9) #double quotes will be in output as it is within single quotes
print('b is {}'.format(b))


c = '"seven {1:<9} {0:>9}"'.format(8,9) #double quotes will be in output as it is within single quotes
print('c is {}'.format(c))

d = '"seven {1:<09} {0:>09}"'.format(8,9) #leading zeros and zeros after
print('d is {}'.format(d))

#what if numbers within format is larger: takes up same amount of space

e = '"seven {1:<09} {0:>09}"'.format(8283,123459) #leading zeros and zeros after
print('d is {}'.format(d)) #this spaces works with f-strings as well. 

x = 0.1 + 0.1 + 0.1 - 0.3
print(x)  #you will notice output is not 0 as float is not accurate for decimal
y = round(x,3) #even with 3 , only outputs 0.0 
print(y) 


#instead do this for cases involving money etc:
from decimal import *
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print(f'x is {x}')
print(type(x))

#for many purposes, the simple integer and float types will work fine
#for cases e.g. involving money decimal mod can be used

#bool type 
#used for logical values and expressions. 

x = True  #or can be False as well 
print('x is {}'.format(x))
print(type(x)) #bool type

y = 7 > 5
print(f'y is {y}')
print(type(y)) #bool type output is true


z = None 
print('z is {}'.format(x))
print(type(z)) #'NoneType'
if z:
    print("True") #numeric value other than those stated below will return True
else:
    print("False") #value of none or 0 or empty string returns False. 










    


a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false') #output as b is false

if a or b:
    print('expression is true') #output as a is true
else:
    print('expression is false')


if y in x:
    print('expression is true') #true as bear is in x
else:
    print('expression is false')


if 'tree' in x:
    print('expression is true')
else:
    print('expression is false') #false as tree not in x


if y is x[0]:
    print('expression is true') #output 
else:
    print('expression is false')

if y is not x[0]:
    print('expression is true') 
else:
    print('expression is false')









"""
Boolean Operators

and     And

or      Or

not     Not

in      Value in set

not in  Value not in set

is      Same object identity

is not  Not same object identity

"""
#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World.{}'.format(42 * 7))

print("""
      Hello,
      World. 
      {}
      
      """.format(42*7))

s - 'Hello, World. {}'
print(s.format(42*7))


class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString('Hello World.')
print(s)


#strings are first class objects in Python


print('Hello World'.upper())
print('Hello World'.lower())
print('Hello World'.capitalize())
print('Hello World'.swapcase())
print('Hello World. g '.casefold() #similar to lower but even more forced used for german words etc like sasse or german streets


s1 = 'Hello World'
s2 = 'Hello World'.upper()

# s1 != s2


x = 42
y = 73
print('the number is {} {}'.format(x,y))
print('the number is {xx} {bb}'.format(xx = x, bb =y))
print('the number is {bb} {xx}'.format(xx = x, bb =y))
print('the number is {1} {0}'.format(x,y))
print('the number is {0} {1} {0}'.format(x,y))
print('the number is {0:<5} {1:>5}'.format(x,y))

print('the number is {0:<5} {1:>05}'.format(x,y))
print('the number is {0:<5} {1:>+05}'.format(x,y))

z = 42 * 747 * 1000
print('the number is {:,}'.format(z).replace(',','.'))
print('the number is {:f}'.format(z))
print('the number is {:.3f}'.format(z))

q = 42
print('the number is {:x}'.format(q)) #hexadecimal
print('the number is {:o}'.format(q)) #octadecmial
print('the number is {:b}'.format(q)) #binary

#f-strings now can be used instead of format
#all above will be applicable for f-strings. 
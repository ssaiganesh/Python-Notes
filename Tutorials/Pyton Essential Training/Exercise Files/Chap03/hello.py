

x = (1 , 'two', 3.0, [4,'four'], 5)
print(f'x is {x}')
print(type(x)) #tuple type
print(type(x[1]))  #str type

#can inspect any element 

x = (1 , 'two', 3.0, [4,'four'], 5)
y = (1 , 'two', 3.0, [4,'four'], 5)
print(f'x is {x}')
print(id(x)) 
print(id(y))
#x and y are of the same type but different ids
#unique idenitifier for different objects

print(id(x[0]))
print(id(y[0]))
#both are same ids as both are number 1
if x[0] is y[0]:
    print("Yes") #returns yes
else:
    print("No")

if x is y:
    print("Yes") 
else:
    print("No") #returns no

#Checking if tuple :
#the below case does not work
if type(x) == "tuple":
    print("Yes")
else:
    print("No") #returns this even if x is tuple

#instead can do this:
if isinstance(x, tuple):
    print("Tuple")
elif isinstance(x, list):
    print("List")
else:
    print("No")
#use isinstance for checking for a specific type
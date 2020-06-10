

print('Hello, World.')

#string functions:

#repr 
#ascii
#chr
#ord



x = (1,2,3,4,5)
length = len(x)
reverse_list = list(reversed(x))
total = sum(x)
sum_ten = sum(x,10)
maximum = max(x)
minimum = min(x)
anything_true = any(x) #if all are zero then will be false
all_true = all(x) #if all are >= 1 then will be True



i = (1,2,3,4,5)
j = (6,7,8,9,10)
k = zip(i,j)
for a,b in k: print(f'{a} - {b}')




t = ("cat", "dog", "rabbit", "velociraptor")
for n,v in enumerate(t): print(f'{n}:{v}')


x = 42
y = type(x)
z = isinstance(x, int) #false if float or any other types

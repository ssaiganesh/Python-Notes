

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals: 
    print(pet) #prints the animlas list one by one until list ends


for pet in range(5):
    print(pet) #prints 0, 1, 2, 3, 4



for pet in animals:
    #if pet == 'dog': continue #skips dog while going through the loop
    #if pet == 'velociraptor': break #doesn't print velociraptor as well
    print(pet)
else:
    print('that is all of the animals') #wouldn't print if break statementis there







#This progra asks user for 8 names of people and store them in a list
#And picks a random one and prints it
import random
people =[]

for x in range (0,8):
    person = input("What is the name of the person?") #initially called this variable people, not possible
    people.append(person) #forgot this line initally to add the person to list

    
guess = random.randint(0,7) # 7 not 8

# just keying in "people[guess]" doesn't print the person like the full list usually does
# for full list can just type people

random_person = people[guess]
print("Picking a random person: ", random_person)


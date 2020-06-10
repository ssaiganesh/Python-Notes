f = open("text file.txt","r") #can omit "r" if just read mode
print(f.read())

f = open("text file.txt","r")
print(f.read())

f = open("text file.txt","w") #opening in write mode
f.write("This text will overwrite the content of the file")
f = open("text file.txt") #opening in read mode
print(f.read())


f = open("text file.txt","a") #append mode
f.write("\nThis text will be appended to the file")
f = open("text file.txt")
print(f.read())


f = open("test2.txt","x") #creates new file. cannot run again as file already exists


#write full path if want to create new file in different folder.




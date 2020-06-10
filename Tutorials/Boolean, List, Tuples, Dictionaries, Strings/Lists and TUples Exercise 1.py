birthday = input("Enter your birthdate in the format DD-MM-YYY:")
months = ("January","February","March","April","May","June","July","August","September","October","November","December")
index = int(birthday[3:5])
print("You were born in",months[index-1])



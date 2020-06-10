person = {"name":"Peter","gender":"male","age":"24","address":"100 Charming Avenue","phone":"12345678"}
index = input("What would you like to know about the person?").lower()
print(person.get(index,"invalid property"))
#case sensitive. To avoid case sensitive in input -- add  .lower to the end

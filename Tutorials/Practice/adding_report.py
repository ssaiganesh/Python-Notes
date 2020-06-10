def adding_report(type_report):
    total = 0
    numbers = "\nItems\n"
    
    while True:
        integer = input("Integer or Quit with Q: ")
        if(integer.isdigit()):
            total += int(integer)
            numbers = numbers +integer + "\n"
        elif(integer.lower() == "q" or integer.lower() == "quit"):
            if(type_report == "A"):
                print(numbers)
                print("\nTotal\n",total)
                break
            else:
                print("Total\n",total)
                break
        else:
            print(integer,"is invalid input")
    
adding_report("A")
adding_report("T")
    
                
            
    
    

def str_analysis(userinput): 
  while userinput == "":
    userinput = input("Enter word or integer: ")
  else:
    if userinput.isdigit():
      if int(userinput) > 99:
        print( int(userinput), "is a pretty big number.")
      elif int(userinput) < 99:
        print(int(userinput),"is a smaller number than expected.")
    elif userinput.isalpha():
      print('"'+userinput+'"', "is all alphabetical characters!")
    else:
      print('"'+userinput+'"', "is of multiple character types.")

str_analysis(input("Enter word or integer: "))

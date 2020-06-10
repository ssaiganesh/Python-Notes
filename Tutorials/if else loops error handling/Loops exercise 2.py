#This program picks a random color from a list and lets the user try to guess it.
#When he does it, ask if he wants to play again.
#Keeps playing until user types "no".

import random

colors = ["red", "yellow", "orange", "green", "blue", "white", "black", "purple", "pink"]

#user_color = input("Guess the color: ")
#random_int = random.randint(0,8) #can use len(colors)-1 instead for second value
#program_color = colors[random_int]

#while True:
 #   if user_color.lower() == program_color.lower():
  #      print("You guessed it. I was thinking about", program_color)
   #     break
    #else:
     #   answer = input("Do you want to play again?")
      #  if(answer.lower() == "no"):
       #                print("Sorry, I was thinking about", program_color)
        #               break
        #elif(answer == "yes"): # this is now wrong because it will still go on infinte loop on if 
         #   user_color = input("Guess the color: ")
          #      continue
        #else:
         #    print("Invalid entry. Key in yes or no")
        #

#___


#answer

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color, can you guess it: ")

    while True:
        if(color == guess.lower()):
            break
        else:
            guess = input("Nope. Try again: ")
    print("You guessed it! I was thinking about", color)

    play_again = input("Let's play again? Type 'no' to quit.")

    if play_again.lower() == 'no':
        break

    print("It was fun, thanks for playing!")


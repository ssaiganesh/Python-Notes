
def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1:5:2]) #similar to range
    i = game.index('Paper') #index method to find where the string is
    print(game[i])
    #list is mutable therefore can be changed
    game.apped('Computer') #inserts string to the end
    game.insert(0,'Computer') #inserts string to whichever position you want
    game.remove('Paper') #removes specific string
    game.pop() #removes last string
    game.pop(3) # removes lizard
    del game[3] #removes lizard (alternate method)
    del game[1:3] #removes paper and scissors
    del game[1:5:2] #removes paper and lizard
    x = game.pop() #takes the value of last value/string
    print(len(game)) #number of strings in list

    print(', '.joing(game)) # adds comma and space between each string in list

    print(x) #Prints the last value/string
    print_list(game)

"""
Note that tuple is similar to list just that it is immutable
thus cannot be changed such as append, remove, etc..
round brackets e.g. game = ('Rock', 'Paper', 'Scissors')
"""

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()

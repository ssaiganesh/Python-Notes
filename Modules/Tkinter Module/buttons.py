from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="You clicked the button!")
    myLabel.pack()


myButton = Button(root, text = "Click Me!", command =myClick, fg= 'blue', bg = 'white') #fg is text color 

#remember not to put myClick() instead of myClick. as the text will appear before button clicked if put parantheses 

#Just to show other arguments in Button():

#myButton = Button(root, text = "Click Me!", command =myClick, padx = 50, pady = 50, state = DISABLED )

myButton.pack()

root.mainloop() #the x on window disrupts the mainloop . 
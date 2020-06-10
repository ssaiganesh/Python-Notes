from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text="My name is Sai Ganesh")

#myLabel1 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
#myLabel2 = Label(root, text="My name is Sai Ganesh").grid(row = 1, column = 5)
#myLabel3 = Label(root, text = "                  ").grid(row = 1, column = 1)

myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 1, column = 5)

root.mainloop() #the x on window disrupts the mainloop . 
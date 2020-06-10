#150 problem exercises
"""
#__________________________________________

print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are")
#__________________________________________
#This program lets you know your system version of python
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#__________________________________________
#This program lets you know the yy-mm-dd hh:mm:ss of current local time

#my answer -- sep="" to remove spaces between commas
import time as t
time_now = t.time()
user_time = t.localtime(time_now)
print(user_time.tm_year, "-" , user_time.tm_mon ,"-", user_time.tm_mday," ",user_time.tm_hour ,":" ,user_time.tm_min, ":" ,user_time.tm_sec,sep="")

#SAMPLE SOLUTION : 
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#__________________________________________
#This program takes in the input of radius and calculates area of circle. 
import math
r = float(input("r:"))
area = math.pi * r **2
print(area) 

#__________________________________________
#This program inputs your first and last name and reverses the string

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name = first_name + " " +last_name
print(name[::-1]) #standard code to reverse string

#the below code was my first try and it is wrong.
# i= 0
# j = len(name)
# for i in range(0,j):
#     name[i] = name[j-1]
#     i += 1
#     j -= 1

# print(name)
#__________________________________________
#The actual exercise for above asked to just print last name first and first name last
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)

#__________________________________________
#Display first and last colour in the list
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[-1])

#the solution:
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1])) #not sure of the purpose of %s here

#__________________________________________
#This program accepts an integer (n) and computes the value of n+nn+nnn.
value  = input("Value of n:" )
second_value = value*2
third_value = value*3 
total = int(value) + int(second_value) + int(third_value) 
print(total)

"""
#__________________________________________

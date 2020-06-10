print("This program calculates the area and circumference of a circle using radius.")
radius = float(input("What is the radius of the circle?"))
#Initially, I made a mistake of not including float in the above code line
import math
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print("The area of the circle is ", area, " and the circumference is ",circumference, ".")

#to round the values above

print("The area of the circle is", round(area,2))
print("The circumeference of the circle is", round(circumference,2))

grade1 = float(input("Type the grade of the first test: "))
grade2 = float(input("Type the grade of the second test: "))
absences = int(input("Type the number of absences: "))
total_classes = int(input("Type the total number of classes: "))

avg_grade = (grade1 + grade2)/2
attendance = (total_classes - absences)/total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance*100),2))+'%') #note have to change to str to add the %


#rules:
#grades are 0 to 10
#students need an average grade of 6 or higher to get approval
#students need an attendance rate of 80% or higher to get approval

if (avg_grade >= 6):
    if(attendance >= 0.8):
        print("The student was approved.")
    else:
        print("The student has failed due to the attendance rate lower than 80%.")
elif(attendance >= 0.8):
    print("The student has failed due to an average grade lower than 6.0.")

else:
    print("The student has failed due to an average grade lower than 6.0 and an attendance rate lower than 80%.")
    

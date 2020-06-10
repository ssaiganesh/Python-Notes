#Data Validation Exercise
#Data validation exercise to avoid errors
#This program is better but still gives errors when strings are given.

data_valid = False

while data_valid == False:
    grade1 = float(input("Type the grade of the first test: "))
    if grade1 < 0 or grade1 > 10:
            print("Grade should be between 0 and 10.")
            continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = float(input("Type the grade of the second test: "))
    if grade2 < 0 or grade2 > 10:
            print("Grade should be between 0 and 10.")
            continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    total_classes = int(input("Type the total number of classes: "))
    if total_classes <= 0:
        print("Classes should be greater than 0.")
        continue
    else:
        data_valid = True

data_valid = False 

while data_valid == False:
    absences = int(input("Type the number of absences: "))
    if absences < 0 or absences > total_classes:
        print("Absenses should be greater than or equal to zero and less than or equal to total number of classes.")
        continue
    else:
        data_valid = True
        


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
    

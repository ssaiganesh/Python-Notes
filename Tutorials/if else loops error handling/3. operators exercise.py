print("This program calculates your body mass index.")

weight = float(input("Your weight in kg: "))
height = float(input("Your weight in meters: "))

bmi = weight / (height ** 2)

if(bmi <= 18.5):
    print("Your BMI is ",round(bmi,1)," and you are underweight.")
elif(bmi > 18.5 and bmi <= 24.9):
    print("Your BMI is ",round(bmi,1)," and you are at a normal weight.")
elif(bmi > 24.9 and bmi <= 29.9):
    print("Your BMI is ",round(bmi,1)," and you are overweight.")
else:
    print("Your BMI is ",round(bmi,1)," and you are obese.")


    

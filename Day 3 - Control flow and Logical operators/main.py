"""Even or odd, BMI Calculator"""

number = int(input("Enter the number to check the number is Odd or Even:"))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi >= 18.5:
    if bmi < 25:
        print("normal weight")
    else:
        print("overweight")
else:
    print("underweight")

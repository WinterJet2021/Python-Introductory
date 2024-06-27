# BMI Calculator

A = int(input("Input your weight: "))
B = int(input("Input your height: "))

def calculate_bmi(weight, height_cm):
    # Convert height from cm to meters
    height_m = height_cm / 100
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    return bmi


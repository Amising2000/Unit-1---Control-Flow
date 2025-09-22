weight = input("Enter your weight: ")
height = input("Enter your height: ")

BMI = (weight / (height * height)) * 703

category = ("Underweight" if BMI < 18.5 else
            "Normal" if 18.5 <= BMI <= 25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese"
            )

print(f"BMI: {category}")
weight = float(input("Enter your weight (in pounds): "))
height = float(input("Enter your height (in inches): "))

BMI = (weight / (height * height)) * 703

category = ("Underweight" if BMI < 18.5 else
            "Normal" if 18.5 <= BMI <= 25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese"
            )

print(f"BMI: {category}")
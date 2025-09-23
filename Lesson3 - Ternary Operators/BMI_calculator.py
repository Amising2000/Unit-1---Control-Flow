weight = float(input("Enter your weight (in pounds): "))
height = float(input("Enter your height (in inches): "))

if height or weight < 0:
    print ("Error, please enter a valid weight or height.")

BMI = (weight / (height * height)) * 703

category = ("Underweight- Gain weight" if BMI < 18.5 else
            "Normal- Maintain weight" if 18.5 <= BMI <= 25 else
            "Overweight- Lose weight" if 25 <= BMI < 30 else
            "Obese"
            )

print(f"Weight: {weight}lb\nHeight: {height}in\nBMI: {category}")
# JS Ternary
'''
let status = age >= 18 ? "adult" : "minor"
let message = score >= 90 ? "Excellent" : "Keep trying"
'''

# Python ternary
age = 15
status = "adult" if age >= 18 else "minor"
score = 75
message = "Excellent" if score >= 90 else "Keep trying"

# Examples
password = "mypass123"
strength = "Strong" if len(password) >= 8 else "Weak"
print(f"Password: {password}\nStrength: {strength}")

# Combining Ternary + Chaining
category = ("Child" if 0 <= age <= 12 else 
            "teen" if 13 <= age <= 17 else
            "Adult" if 18 <= age <= 64 else
            "Senior"
            )

score = 89
grade = ("A" if 100 >= score >= 90 else
         "B" if 89 >= score >= 80 else
         "C" if 79 >= score >= 70 else
         "D" if 69 >= score >= 60 else
         "F"
         )
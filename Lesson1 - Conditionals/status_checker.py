# Student Information System - Starter Code
print("STUDENT INFORMATION SYSTEM")
print("========================================")

# Get student information
student_name = input("Enter your full name: ")
student_age = input("Enter your age: ")
student_GPA = input("Enter your GPA: ")

age=int(student_age)
gpa=float(student_GPA)
# Show student information
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"GPA: {student_GPA}")

# TODO: Check if age is valid (between 16 and 100)


# TODO: Check if GPA is valid (between 0.0 and 4.0)


# TODO: Check enrollment eligibility (age >= 18 AND gpa >= 2.0)
if age >= 18 and gpa >= 2.0:
    print("✅ ELIGIBLE for enrollment")
else:
    print("❌ NOT ELIGIBLE for enrollment")

# TODO: Check voting eligibility (age >= 18)
if age >= 18:
    print("✅ ELIGIBLE to vote")
else:
    print("❌ NOT ELIGIBLE to vote")

# TODO: Check honor roll status (gpa >= 3.5)
if gpa >= 3.5:
    print("🏆 ON HONOR ROLL")
else:
    print("📚 NOT ON HONOR ROLL")